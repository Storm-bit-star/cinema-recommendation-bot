"""
Google Gemini API Client
"""

import os
import google.generativeai as genai


class GeminiClient:
    """Client for interacting with Google Gemini API."""
    
    def __init__(self):
        """Initialize Gemini client with API key."""
        api_key = os.getenv('GEMINI_API_KEY')
        
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
    
    def get_recommendation(self, prompt: str) -> str:
        """
        Get recommendation from Gemini API.
        
        Args:
            prompt (str): Input prompt for Gemini
            
        Returns:
            str: Recommendation response from Gemini
        """
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            raise Exception(f"Error getting recommendation from Gemini: {str(e)}")
    
    def analyze_request(self, user_request: str) -> dict:
        """
        Analyze user request to extract key information.
        
        Args:
            user_request (str): User's request text
            
        Returns:
            dict: Extracted information (genres, mood, etc.)
        """
        analysis_prompt = f"""Analyze this user request for film/TV recommendations and extract key information:

User Request: "{user_request}"

Provide a JSON response with:
- intent: what type of recommendation is being requested
- genres: potential genres mentioned or implied
- mood: emotional tone or mood requested
- keywords: main keywords from the request
- media_type: "film", "series", or "both"

Response format:
{{"intent": "", "genres": [], "mood": "", "keywords": [], "media_type": ""}}"""
        
        response = self.model.generate_content(analysis_prompt)
        
        try:
            import json
            return json.loads(response.text)
        except:
            return {
                'intent': 'general',
                'genres': [],
                'mood': 'unknown',
                'keywords': user_request.split(),
                'media_type': 'both'
            }
