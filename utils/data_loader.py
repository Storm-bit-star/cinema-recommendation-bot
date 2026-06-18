"""
Data Loader - Loads and manages cinema data
"""

import json
import os
from typing import List, Dict


class DataLoader:
    """Loads cinema data from local JSON files."""
    
    def __init__(self):
        """Initialize data loader."""
        self.data_dir = 'data'
        self._ensure_data_dir()
    
    def load_films(self) -> List[Dict]:
        """
        Load films data.
        
        Returns:
            List[Dict]: List of films
        """
        try:
            filepath = os.path.join(self.data_dir, 'films.json')
            if os.path.exists(filepath):
                with open(filepath, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception as e:
            print(f"Error loading films: {e}")
        
        return self._get_default_films()
    
    def load_tv_series(self) -> List[Dict]:
        """
        Load TV series data.
        
        Returns:
            List[Dict]: List of TV series
        """
        try:
            filepath = os.path.join(self.data_dir, 'tv_series.json')
            if os.path.exists(filepath):
                with open(filepath, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception as e:
            print(f"Error loading TV series: {e}")
        
        return self._get_default_tv_series()
    
    def save_films(self, films: List[Dict]) -> bool:
        """
        Save films data.
        
        Args:
            films (List[Dict]): Films to save
            
        Returns:
            bool: Success status
        """
        try:
            filepath = os.path.join(self.data_dir, 'films.json')
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(films, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error saving films: {e}")
            return False
    
    def save_tv_series(self, series: List[Dict]) -> bool:
        """
        Save TV series data.
        
        Args:
            series (List[Dict]): TV series to save
            
        Returns:
            bool: Success status
        """
        try:
            filepath = os.path.join(self.data_dir, 'tv_series.json')
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(series, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error saving TV series: {e}")
            return False
    
    def _ensure_data_dir(self):
        """Ensure data directory exists."""
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
    
    def _get_default_films(self) -> List[Dict]:
        """
        Get default sample films data.
        
        Returns:
            List[Dict]: Sample films
        """
        return [
            {
                "id": "tt1375666",
                "title": "Inception",
                "year": 2010,
                "genres": ["Sci-Fi", "Thriller", "Action"],
                "rating": 8.8,
                "plot": "A skilled thief who steals corporate secrets through shared dreaming technology",
                "director": "Christopher Nolan",
                "cast": ["Leonardo DiCaprio", "Marion Cotillard", "Joseph Gordon-Levitt"],
                "runtime": 148,
                "imdbRating": 8.8,
                "streamingOn": ["Netflix", "Prime Video"]
            },
            {
                "id": "tt0111161",
                "title": "The Shawshank Redemption",
                "year": 1994,
                "genres": ["Drama"],
                "rating": 9.3,
                "plot": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency",
                "director": "Frank Darabont",
                "cast": ["Tim Robbins", "Morgan Freeman"],
                "runtime": 142,
                "imdbRating": 9.3,
                "streamingOn": ["Netflix"]
            }
        ]
    
    def _get_default_tv_series(self) -> List[Dict]:
        """
        Get default sample TV series data.
        
        Returns:
            List[Dict]: Sample TV series
        """
        return [
            {
                "id": "tt0944947",
                "title": "Game of Thrones",
                "genres": ["Drama", "Fantasy"],
                "seasons": 8,
                "episodes": 73,
                "rating": 9.2,
                "plot": "Nine noble families fight for control of the Seven Kingdoms",
                "streamingOn": ["HBO Max"]
            },
            {
                "id": "tt0903747",
                "title": "Breaking Bad",
                "genres": ["Crime", "Drama", "Thriller"],
                "seasons": 5,
                "episodes": 62,
                "rating": 9.5,
                "plot": "A chemistry teacher turned methamphetamine producer",
                "streamingOn": ["Netflix"]
            }
        ]
