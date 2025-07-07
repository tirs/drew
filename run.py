#!/usr/bin/env python3
"""
🚀 Advanced Trade Station Dashboard
Bootstrap Version - Optimized & Organized
"""

import os
import sys
from app import app

def main():
    """Run the Flask application"""
    print("🚀 Starting Advanced Trade Station Dashboard (Bootstrap Version)")
    print("📊 Features:")
    print("   ✅ 8 Open Trades + 25 Recent Trades")
    print("   ✅ Dark/Grey Theme with Glass Morphism")
    print("   ✅ Advanced UI with Smooth Animations")
    print("   ✅ Dashboard & JSON API Toggle")
    print("   ✅ Real-time Updates Every 30s")
    print("   ✅ Mobile Responsive Design")
    print("   ✅ Optimized Code Structure")
    print()
    print("🌐 Access URLs:")
    print("   📊 Dashboard: http://localhost:5000")
    print("   🔗 API:       http://localhost:5000/api")
    print()
    print("💡 Tips:")
    print("   • Click 'View JSON' button to toggle API view")
    print("   • Dashboard auto-refreshes every 30 seconds")
    print("   • Hover over cards for smooth animations")
    print()
    print("Press Ctrl+C to stop the server")
    print("=" * 60)
    
    try:
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n👋 Server stopped. Thanks for using Trade Station!")
        sys.exit(0)

if __name__ == '__main__':
    main()