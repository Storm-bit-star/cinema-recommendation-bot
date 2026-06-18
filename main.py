"""
Cinema Recommendation Bot - Main Entry Point
"""

import os
import sys
from dotenv import load_dotenv
from bot import CinemaRecommendationBot

# Load environment variables
load_dotenv()


def main():
    """Main function to run the cinema recommendation bot."""
    
    # Check for required API keys
    gemini_key = os.getenv('GEMINI_API_KEY')
    if not gemini_key:
        print("❌ Error: GEMINI_API_KEY not found in .env file")
        print("Please set up your .env file with the required API keys")
        sys.exit(1)
    
    print("🎬 Cinema Recommendation Bot Started!")
    print("=" * 50)
    print("Type 'exit' to quit")
    print("=" * 50)
    
    # Initialize the bot
    try:
        bot = CinemaRecommendationBot()
        print("✅ Bot initialized successfully\n")
    except Exception as e:
        print(f"❌ Error initializing bot: {e}")
        sys.exit(1)
    
    # Interactive loop
    while True:
        try:
            user_input = input("\n🎭 What kind of film or series are you looking for?\n> ").strip()
            
            if user_input.lower() in ['exit', 'quit', 'q']:
                print("\n👋 Thanks for using Cinema Recommendation Bot!")
                break
            
            if not user_input:
                print("⚠️  Please enter a valid request")
                continue
            
            print("\n⏳ Generating recommendations...\n")
            recommendation = bot.recommend(user_input)
            
            print("=" * 50)
            print(recommendation)
            print("=" * 50)
            
        except KeyboardInterrupt:
            print("\n\n👋 Bot interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            print("Please try again with a different request.\n")


if __name__ == "__main__":
    main()
