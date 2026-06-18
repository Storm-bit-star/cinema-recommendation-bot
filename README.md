# 🎬 Cinema Recommendation Bot

An AI-powered film and TV series recommendation bot built with **Google Gemini API**. This bot analyzes cinema, TV series, and film data to provide personalized recommendations based on user requests.

## ✨ Features

- 🤖 **AI-Powered Recommendations** - Uses Google Gemini API for intelligent suggestions
- 🎬 **Dual Support** - Recommends both films and TV series
- 🔍 **Multiple Query Types**:
  - Genre-based recommendations
  - Actor/Director-based search
  - Mood-based suggestions
  - Similar title recommendations
  - Platform availability checks
- 📊 **Rich Data Integration** - Pulls from TMDB, OMDb, and other cinema databases
- 🌐 **Streaming Platform Info** - Shows where to watch recommended content
- 💾 **Local Caching** - Efficient data management

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Google Cloud Account with Gemini API access
- API keys for TMDB and/or OMDb (optional but recommended)

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/Storm-bit-star/cinema-recommendation-bot.git
cd cinema-recommendation-bot
```

2. **Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables:**
```bash
cp .env.example .env
# Edit .env and add your API keys:
# - GEMINI_API_KEY
# - TMDB_API_KEY (optional)
# - OMDB_API_KEY (optional)
```

### Usage

```python
from bot import CinemaRecommendationBot

# Initialize the bot
bot = CinemaRecommendationBot()

# Get recommendations
recommendation = bot.recommend("I want a sci-fi thriller like Inception")
print(recommendation)
```

### Example Queries

- "Recommend me something like Breaking Bad"
- "Show me the best horror films from the last 5 years"
- "What Leonardo DiCaprio films can I watch on Netflix?"
- "I'm in the mood for a feel-good comedy"
- "Find me Christopher Nolan's filmography"

## 📁 Project Structure

```
cinema-recommendation-bot/
├── main.py                 # Entry point
├── bot.py                  # Core recommendation logic
├── data/
│   ├── films.json         # Sample film database
│   ├── tv_series.json     # Sample TV series database
│   └── schema.json        # Data structure template
├── api/
│   ├── gemini_client.py   # Gemini API integration
│   ├── tmdb_client.py     # TMDB API integration
│   └── omdb_client.py     # OMDb API integration
├── utils/
│   ├── data_loader.py     # Load and manage cinema data
│   └── formatters.py      # Format recommendation output
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory:

```
GEMINI_API_KEY=your_gemini_api_key_here
TMDB_API_KEY=your_tmdb_api_key_here
OMDB_API_KEY=your_omdb_api_key_here
DEBUG=False
```

### Gemini API Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable the Generative AI API
4. Create an API key
5. Add it to your `.env` file

### TMDB API Setup (Recommended)

1. Visit [TMDB API](https://www.themoviedb.org/settings/api)
2. Create a free account
3. Request an API key
4. Add it to your `.env` file

## 📊 Data Format

The bot expects cinema data in the following JSON format:

```json
{
  "films": [
    {
      "id": "tt1375666",
      "title": "Inception",
      "year": 2010,
      "genres": ["Sci-Fi", "Thriller", "Action"],
      "rating": 8.8,
      "plot": "A skilled thief who steals corporate secrets through shared dreaming...",
      "director": "Christopher Nolan",
      "cast": ["Leonardo DiCaprio", "Marion Cotillard", "Joseph Gordon-Levitt"],
      "runtime": 148,
      "imdbRating": 8.8,
      "streamingOn": ["Netflix", "Prime Video"]
    }
  ],
  "tvSeries": [
    {
      "id": "tt0944947",
      "title": "Game of Thrones",
      "genres": ["Drama", "Fantasy"],
      "seasons": 8,
      "episodes": 73,
      "rating": 9.2,
      "plot": "Nine noble families fight for control of the Seven Kingdoms...",
      "streamingOn": ["HBO Max"]
    }
  ]
}
```

## 🤖 How It Works

1. **User Input**: User provides a recommendation request
2. **Data Retrieval**: Bot retrieves relevant cinema data from local/API sources
3. **Gemini Processing**: Request is sent to Gemini API with context
4. **Recommendation Generation**: AI generates personalized recommendations
5. **Output Formatting**: Results are formatted with streaming info and explanations
6. **User Display**: Recommendations are presented to the user

## 📚 API Documentation

### CinemaRecommendationBot Class

```python
class CinemaRecommendationBot:
    def recommend(user_request: str) -> str
    def search_by_genre(genre: str, limit: int = 5) -> list
    def search_by_actor(actor_name: str, limit: int = 5) -> list
    def search_by_director(director_name: str, limit: int = 5) -> list
    def search_similar(title: str, media_type: str = "film") -> list
```

## 🧪 Testing

```bash
# Run tests
python -m pytest tests/

# Run with verbose output
python -m pytest tests/ -v
```

## 🛠️ Development

### Adding New Data Sources

Edit `api/` directory to add new cinema data sources:

```python
# Example: api/new_source_client.py
class NewSourceClient:
    def get_films(self, query: str):
        pass
```

### Extending Recommendation Logic

Modify `bot.py` to customize recommendation algorithms:

```python
def custom_recommendation_logic(user_request: str):
    # Your custom logic here
    pass
```

## 🐛 Troubleshooting

**Q: "API key not found" error**
- A: Make sure `.env` file exists and contains your API keys

**Q: Slow recommendations**
- A: Check internet connection and API rate limits

**Q: No data loading**
- A: Verify JSON files in `data/` directory are properly formatted

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [Google Gemini API](https://ai.google.dev/) - AI recommendations engine
- [TMDB API](https://www.themoviedb.org/settings/api) - Cinema data
- [OMDb API](http://www.omdbapi.com/) - Movie information

## 📞 Support

For issues and questions:
- Open an [Issue](https://github.com/Storm-bit-star/cinema-recommendation-bot/issues)
- Check existing discussions
- Review documentation

---

**Made with ❤️ by Storm-bit-star**
