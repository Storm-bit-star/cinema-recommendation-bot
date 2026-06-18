"""
Formatters - Format recommendations output
"""

from typing import Dict, List


class RecommendationFormatter:
    """Formats recommendation output."""
    
    @staticmethod
    def format_film(film: Dict) -> str:
        """
        Format a film for display.
        
        Args:
            film (Dict): Film data
            
        Returns:
            str: Formatted film string
        """
        output = f"\n🎬 {film.get('title', 'Unknown')} ({film.get('year', 'N/A')})\n"
        output += f"   ⭐ Rating: {film.get('rating', 'N/A')}\n"
        output += f"   🎭 Director: {film.get('director', 'Unknown')}\n"
        output += f"   🏷️  Genres: {', '.join(film.get('genres', []))}\n"
        output += f"   ⏱️  Runtime: {film.get('runtime', 'N/A')} minutes\n"
        output += f"   📝 Plot: {film.get('plot', 'N/A')[:150]}...\n"
        
        streaming = film.get('streamingOn', [])
        if streaming:
            output += f"   📺 Watch on: {', '.join(streaming)}\n"
        
        return output
    
    @staticmethod
    def format_series(series: Dict) -> str:
        """
        Format a TV series for display.
        
        Args:
            series (Dict): Series data
            
        Returns:
            str: Formatted series string
        """
        output = f"\n📺 {series.get('title', 'Unknown')}\n"
        output += f"   ⭐ Rating: {series.get('rating', 'N/A')}\n"
        output += f"   🏷️  Genres: {', '.join(series.get('genres', []))}\n"
        output += f"   🎬 Seasons: {series.get('seasons', 'N/A')} | Episodes: {series.get('episodes', 'N/A')}\n"
        output += f"   📝 Plot: {series.get('plot', 'N/A')[:150]}...\n"
        
        streaming = series.get('streamingOn', [])
        if streaming:
            output += f"   📺 Watch on: {', '.join(streaming)}\n"
        
        return output
    
    @staticmethod
    def format_recommendations(recommendations: List[Dict], media_type: str = 'mixed') -> str:
        """
        Format multiple recommendations for display.
        
        Args:
            recommendations (List[Dict]): List of recommendations
            media_type (str): Type of media ('film', 'series', or 'mixed')
            
        Returns:
            str: Formatted recommendations string
        """
        if not recommendations:
            return "No recommendations found."
        
        output = "\n" + "=" * 60 + "\n"
        output += "🎯 RECOMMENDATIONS\n"
        output += "=" * 60
        
        for i, rec in enumerate(recommendations, 1):
            if rec.get('seasons'):  # It's a series
                output += RecommendationFormatter.format_series(rec)
            else:  # It's a film
                output += RecommendationFormatter.format_film(rec)
        
        output += "\n" + "=" * 60 + "\n"
        return output
