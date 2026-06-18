"""
TMDB (The Movie Database) API Client
"""

import os
import requests
from typing import List, Dict, Optional


class TMDBClient:
    """Client for TMDB API to fetch cinema data."""
    
    def __init__(self):
        """Initialize TMDB client."""
        self.api_key = os.getenv('TMDB_API_KEY')
        self.base_url = 'https://api.themoviedb.org/3'
    
    def search_movies(self, query: str, limit: int = 10) -> List[Dict]:
        """
        Search for movies on TMDB.
        
        Args:
            query (str): Search query
            limit (int): Maximum number of results
            
        Returns:
            List[Dict]: List of movies
        """
        if not self.api_key:
            return []
        
        try:
            url = f"{self.base_url}/search/movie"
            params = {
                'api_key': self.api_key,
                'query': query,
                'page': 1
            }
            
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()
            
            data = response.json()
            return data.get('results', [])[:limit]
        except Exception as e:
            print(f"Error searching TMDB movies: {e}")
            return []
    
    def search_tv_series(self, query: str, limit: int = 10) -> List[Dict]:
        """
        Search for TV series on TMDB.
        
        Args:
            query (str): Search query
            limit (int): Maximum number of results
            
        Returns:
            List[Dict]: List of TV series
        """
        if not self.api_key:
            return []
        
        try:
            url = f"{self.base_url}/search/tv"
            params = {
                'api_key': self.api_key,
                'query': query,
                'page': 1
            }
            
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()
            
            data = response.json()
            return data.get('results', [])[:limit]
        except Exception as e:
            print(f"Error searching TMDB TV series: {e}")
            return []
    
    def get_popular_movies(self, limit: int = 20) -> List[Dict]:
        """
        Get popular movies from TMDB.
        
        Args:
            limit (int): Maximum number of results
            
        Returns:
            List[Dict]: List of popular movies
        """
        if not self.api_key:
            return []
        
        try:
            url = f"{self.base_url}/movie/popular"
            params = {
                'api_key': self.api_key,
                'page': 1
            }
            
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()
            
            data = response.json()
            return data.get('results', [])[:limit]
        except Exception as e:
            print(f"Error fetching popular movies: {e}")
            return []
    
    def get_popular_tv_series(self, limit: int = 20) -> List[Dict]:
        """
        Get popular TV series from TMDB.
        
        Args:
            limit (int): Maximum number of results
            
        Returns:
            List[Dict]: List of popular TV series
        """
        if not self.api_key:
            return []
        
        try:
            url = f"{self.base_url}/tv/popular"
            params = {
                'api_key': self.api_key,
                'page': 1
            }
            
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()
            
            data = response.json()
            return data.get('results', [])[:limit]
        except Exception as e:
            print(f"Error fetching popular TV series: {e}")
            return []
