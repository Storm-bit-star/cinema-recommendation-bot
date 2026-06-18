"""
OMDb (Open Movie Database) API Client
"""

import os
import requests
from typing import Dict, Optional


class OMDBClient:
    """Client for OMDb API to fetch movie information."""
    
    def __init__(self):
        """Initialize OMDb client."""
        self.api_key = os.getenv('OMDB_API_KEY')
        self.base_url = 'http://www.omdbapi.com'
    
    def search(self, query: str, media_type: str = 'all') -> Optional[Dict]:
        """
        Search for a movie or series.
        
        Args:
            query (str): Search query
            media_type (str): 'movie', 'series', or 'all'
            
        Returns:
            Dict: Movie/Series information or None if not found
        """
        if not self.api_key:
            return None
        
        try:
            params = {
                'apikey': self.api_key,
                's': query,
                'type': media_type if media_type != 'all' else None
            }
            
            # Remove None values
            params = {k: v for k, v in params.items() if v is not None}
            
            response = requests.get(self.base_url, params=params, timeout=5)
            response.raise_for_status()
            
            data = response.json()
            
            if data.get('Response') == 'True':
                return data.get('Search', [])[0] if data.get('Search') else None
            return None
        except Exception as e:
            print(f"Error searching OMDb: {e}")
            return None
    
    def get_by_id(self, imdb_id: str) -> Optional[Dict]:
        """
        Get detailed information by IMDb ID.
        
        Args:
            imdb_id (str): IMDb ID (e.g., 'tt0111161')
            
        Returns:
            Dict: Detailed movie/series information or None
        """
        if not self.api_key:
            return None
        
        try:
            params = {
                'apikey': self.api_key,
                'i': imdb_id,
                'plot': 'full'
            }
            
            response = requests.get(self.base_url, params=params, timeout=5)
            response.raise_for_status()
            
            data = response.json()
            
            if data.get('Response') == 'True':
                return data
            return None
        except Exception as e:
            print(f"Error fetching from OMDb: {e}")
            return None
