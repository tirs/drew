# 🚀 Advanced Trade Station Dashboard - Bootstrap Version

A sophisticated Flask application with a stunning dark-themed dashboard for trading data visualization, optimized and organized in the bootstrap folder.

## ✨ Features

✅ **Advanced Dark Theme** - Professional dark/grey UI with glass morphism effects  
✅ **Modern Design** - Inter font, smooth animations, and hover effects  
✅ **Comprehensive Data** - 8 open trades + 25 recent closed trades  
✅ **Rich Trade Details** - Margin usage, direction, confidence score, equity, risk levels  
✅ **Interactive Dashboard** - Beautiful cards, progress bars, and responsive tables  
✅ **JSON API** - `/api` endpoint with complete trade data  
✅ **Seamless Toggle** - Switch between dashboard and raw JSON view  
✅ **Real-time Updates** - Auto-refresh every 30 seconds  
✅ **Mobile Responsive** - Optimized for all screen sizes  
✅ **Optimized Code** - Clean, short, and maintainable codebase

## 🚀 Quick Start

1. **Navigate to Bootstrap Folder**
   ```bash
   cd bootstrap
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the App**
   ```bash
   python run.py
   ```
   
   Or directly:
   ```bash
   python app.py
   ```

4. **Access the Dashboard**
   - 📊 Dashboard: http://localhost:5000
   - 🔗 API: http://localhost:5000/api

## 📁 File Structure

```
bootstrap/
├── app.py              # Main Flask application
├── run.py              # Enhanced startup script
├── requirements.txt    # Python dependencies
├── templates/
│   └── dashboard.html  # Advanced dashboard template
└── README.md          # This file
```

## 🎨 Design Features

- **Glass Morphism**: Modern frosted glass effect with backdrop blur
- **Smooth Animations**: Fade-in effects and hover transitions
- **Color-Coded Data**: Green for profits/long, red for losses/short
- **Progress Indicators**: Animated confidence score bars
- **Professional Typography**: Inter font family for clean readability
- **Responsive Grid**: CSS Grid layout that adapts to any screen size

## 🔧 Technical Features

- **Real-time Updates**: Auto-refresh every 30 seconds
- **Interactive Toggle**: Seamless switch between dashboard and JSON views
- **Advanced Styling**: CSS custom properties and modern design patterns
- **Performance Optimized**: Efficient data rendering and smooth interactions
- **Clean Code**: Short, optimized functions for easy maintenance

## 📊 API Response Structure

```json
{
  "timestamp": "2024-01-01T12:00:00",
  "open_trades": [...],
  "recent_trades": [...],
  "summary": {
    "total_open_trades": 8,
    "total_recent_trades": 25,
    "total_open_pnl": 1250.00,
    "total_margin_used": 125000.00,
    "avg_confidence": 82.5
  }
}
```

## 📈 Trade Data Fields

- **ID**: Unique trade identifier (T1000-T1007 for open, T2000-T2024 for recent)
- **Symbol**: Stock/ETF symbol (SPY, QQQ, AAPL, TSLA, etc.)
- **Direction**: Long or Short position
- **Entry/Exit Price**: Trade execution prices
- **P&L**: Profit/Loss calculation with percentage
- **Margin Used**: Required margin for the trade
- **Confidence Score**: Algorithm confidence (60-95%)
- **Risk Level**: Low, Medium, or High risk assessment
- **Equity**: Account equity at trade time
- **Duration**: Time held in position
- **Timestamps**: Entry and exit times

## 🎯 Key Improvements

- **Organized Structure**: All files in dedicated bootstrap folder
- **Enhanced UI**: Glass morphism effects and smooth animations
- **Better Data**: Added risk levels, P&L percentages, and duration
- **Optimized Code**: Shorter, cleaner functions
- **Professional Design**: Dark theme with modern styling
- **Mobile First**: Responsive design for all devices

## 🛠️ Customization

The dashboard is built with CSS custom properties, making it easy to customize:

```css
:root {
    --bg-primary: #0d1117;      /* Main background */
    --accent-blue: #58a6ff;     /* Primary accent */
    --accent-green: #3fb950;    /* Success/profit color */
    --accent-red: #f85149;      /* Error/loss color */
}
```

## 📱 Mobile Support

The dashboard is fully responsive with:
- Adaptive grid layouts
- Touch-friendly buttons
- Optimized typography
- Smooth scrolling

---

**Built with Flask, Bootstrap 5.3, and modern web technologies for the best trading dashboard experience.**