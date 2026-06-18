"""
Core Cinema Recommendation Bot Logic
"""

import os
import json
from typing import List, Dict, Optional
from api.gemini_client import GeminiClient
from utils.data_loader import DataLoader
from utils.formatters import RecommendationFormatter


class CinemaRecommendationBot:
    """
    Main bot class for cinema recommendations.
    Uses Google Gemini API to analyze user requests and provide intelligent recommendations.
    """
    
    def __init__(self):
        """Initialize the recommendation bot."""
        self.gemini_client = GeminiClient()
        self.data_loader = DataLoader()
        self.formatter = RecommendationFormatter()
        
        # Load cinema data
        self.films = self.data_loader.load_films()
        self.tv_series = self.data_loader.load_tv_series()
        
        print("📚 Cinema database loaded")
        print(f"   - Films: {len(self.films)}")
        print(f"   - TV Series: {len(self.tv_series)}")
    
    def recommend(self, user_request: str) -> str:
        """
        Generate recommendations based on user request.
        
        Args:
            user_request (str): User's recommendation request
            
        Returns:
            str: Formatted recommendations from Gemini API
        """
        
        # Prepare context with cinema data
        context = self._prepare_context()
        
        # Create prompt for Gemini
        prompt = self._create_prompt(user_request, context)
        
        # Get recommendation from Gemini
        recommendation = self.gemini_client.get_recommendation(prompt)
        
        return recommendation
    
    def search_by_genre(self, genre: str, limit: int = 5) -> List[Dict]:
        """
        Search films and series by genre.
        
        Args:
            genre (str): Genre to search for
            limit (int): Maximum number of results
            
        Returns:
            List[Dict]: Matching films and series
        """
        results = []
        
        # Search films
        for film in self.films[:limit]:
            if genre.lower() in [g.lower() for g in film.get('genres', [])]:
                results.append(film)
        
        # Search TV series
        for series in self.tv_series[:limit]:
            if genre.lower() in [g.lower() for g in series.get('genres', [])]:
                results.append(series)
        
        return results[:limit]
    
    def search_by_actor(self, actor_name: str, limit: int = 5) -> List[Dict]:
        """
        Search films and series by actor name.
        
        Args:
            actor_name (str): Actor name to search for
            limit (int): Maximum number of results
            
        Returns:
            List[Dict]: Matching films and series
        """
        results = []
        actor_lower = actor_name.lower()
        
        # Search films
        for film in self.films:
            if any(actor_lower in actor.lower() for actor in film.get('cast', [])):
                results.append(film)
        
        # Search TV series
        for series in self.tv_series:
            if any(actor_lower in actor.lower() for actor in series.get('cast', [])):
                results.append(series)
        
        return results[:limit]
    
    def search_by_director(self, director_name: str, limit: int = 5) -> List[Dict]:
        """
        Search films by director name.
        
        Args:
            director_name (str): Director name to search for
            limit (int): Maximum number of results
            
        Returns:
            List[Dict]: Matching films
        """
        results = []
        director_lower = director_name.lower()
        
        for film in self.films:
            if director_lower in film.get('director', '').lower():
                results.append(film)
        
        return results[:limit]
    
    def search_similar(self, title: str, media_type: str = "film", limit: int = 5) -> List[Dict]:
        """
        Find similar films or series.
        
        Args:
            title (str): Title to find similar content for
            media_type (str): "film" or "series"
            limit (int): Maximum number of results
            
        Returns:
            List[Dict]: Similar content
        """
        data = self.films if media_type.lower() == "film" else self.tv_series
        
        # Find the target item
        target = None
        for item in data:
            if item.get('title', '').lower() == title.lower():
                target = item
                break
        
        if not target:
            return []
        
        # Find similar items based on genre
        similar = []
        target_genres = set(g.lower() for g in target.get('genres', []))
        
        for item in data:
            if item.get('title') == target.get('title'):
                continue
            
            item_genres = set(g.lower() for g in item.get('genres', []))
            
            # Calculate genre overlap
            overlap = len(target_genres & item_genres)
            
            if overlap > 0:
                similar.append((overlap, item))
        
        # Sort by overlap and return
        similar.sort(key=lambda x: x[0], reverse=True)
        return [item for _, item in similar[:limit]]
    
    def _prepare_context(self) -> str:
        """
        Prepare cinema data context for Gemini.
        
        Returns:
            str: JSON string with cinema data
        """
        # Prepare a subset of data for context (top rated)
        top_films = sorted(self.films, key=lambda x: x.get('rating', 0), reverse=True)[:10]
        top_series = sorted(self.tv_series, key=lambda x: x.get('rating', 0), reverse=True)[:10]
        
        context = {
            'top_films': top_films,
            'top_series': top_series,
            'total_films': len(self.films),
            'total_series': len(self.tv_series)
        }
        
        return json.dumps(context, indent=2)
    
    def _create_prompt(self, user_request: str, context: str) -> str:
        """
        Create a prompt for Gemini API.
        
        Args:
            user_request (str): User's request
            context (str): Cinema data context
            
        Returns:
            str: Formatted prompt for Gemini
        """
        prompt = f"""You are an expert film and TV series recommendation bot.

CINEMA DATABASE (Summary):
{context}

USER REQUEST: {user_request}

Based on the user's request and the cinema database provided, generate personalized recommendations:

1. Suggest 3-5 films or TV series that match the user's request
2. For each recommendation, include:
   - Title and release year
   - Genre
   - IMDb/Rating score
   - Brief explanation of why it matches the request
   - Where to watch it (if available in database)
3. Be conversational and enthusiastic!
4. Provide useful insights about the recommendations

Format your response in a clear, readable manner."""
        
        return prompt
