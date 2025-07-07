from flask import Flask, render_template, jsonify
import random
import os
from datetime import datetime, timedelta

app = Flask(__name__)

# Production config
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'railway-secret-key-2024')
app.config['ENV'] = os.environ.get('FLASK_ENV', 'production')

# Security: Remove server headers that might expose information
@app.after_request
def remove_server_header(response):
    response.headers.pop('Server', None)
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

def generate_trade_data():
    """Generate realistic trade data"""
    symbols = ['SPY', 'QQQ', 'IWM', 'DIA', 'VTI', 'AAPL', 'MSFT', 'GOOGL', 'TSLA', 'NVDA', 'AMD', 'META']
    
    # Generate 8 open trades
    open_trades = []
    for i in range(8):
        entry_price = round(random.uniform(400, 500), 2)
        current_price = round(entry_price * random.uniform(0.95, 1.05), 2)
        direction = random.choice(['long', 'short'])
        
        if direction == 'long':
            pnl = (current_price - entry_price) * 100
        else:
            pnl = (entry_price - current_price) * 100
            
        trade = {
            'id': f'T{1000 + i}',
            'symbol': random.choice(symbols),
            'direction': direction,
            'entry_price': entry_price,
            'current_price': current_price,
            'quantity': random.randint(50, 500),
            'margin_used': round(random.uniform(5000, 25000), 2),
            'confidence_score': round(random.uniform(65, 95), 1),
            'equity': round(random.uniform(50000, 200000), 2),
            'pnl': round(pnl, 2),
            'pnl_percentage': round((pnl / (entry_price * 100)) * 100, 2),
            'entry_time': (datetime.now() - timedelta(hours=random.randint(1, 48))).strftime('%Y-%m-%d %H:%M:%S'),
            'duration': f"{random.randint(1, 48)}h {random.randint(1, 59)}m",
            'risk_level': random.choice(['Low', 'Medium', 'High']),
            'status': 'open'
        }
        open_trades.append(trade)
    
    # Generate 25 recent closed trades
    recent_trades = []
    for i in range(25):
        entry_price = round(random.uniform(400, 500), 2)
        exit_price = round(entry_price * random.uniform(0.90, 1.10), 2)
        direction = random.choice(['long', 'short'])
        
        if direction == 'long':
            pnl = (exit_price - entry_price) * 100
        else:
            pnl = (entry_price - exit_price) * 100
            
        trade = {
            'id': f'T{2000 + i}',
            'symbol': random.choice(symbols),
            'direction': direction,
            'entry_price': entry_price,
            'exit_price': exit_price,
            'quantity': random.randint(50, 500),
            'margin_used': round(random.uniform(5000, 25000), 2),
            'confidence_score': round(random.uniform(60, 95), 1),
            'equity': round(random.uniform(50000, 200000), 2),
            'pnl': round(pnl, 2),
            'pnl_percentage': round((pnl / (entry_price * 100)) * 100, 2),
            'entry_time': (datetime.now() - timedelta(days=random.randint(1, 30))).strftime('%Y-%m-%d %H:%M:%S'),
            'exit_time': (datetime.now() - timedelta(days=random.randint(0, 29))).strftime('%Y-%m-%d %H:%M:%S'),
            'duration': f"{random.randint(1, 72)}h {random.randint(1, 59)}m",
            'risk_level': random.choice(['Low', 'Medium', 'High']),
            'status': 'closed'
        }
        recent_trades.append(trade)
    
    return open_trades, recent_trades

@app.route('/health')
def health_check():
    """Simple health check endpoint"""
    return {'status': 'healthy', 'timestamp': datetime.now().isoformat()}, 200

@app.route('/')
@app.route('/drew/')
def dashboard():
    """Main dashboard view"""
    open_trades, recent_trades = generate_trade_data()
    
    # Calculate summary stats
    total_open_pnl = sum(trade['pnl'] for trade in open_trades)
    total_margin_used = sum(trade['margin_used'] for trade in open_trades)
    avg_confidence = round(sum(trade['confidence_score'] for trade in open_trades) / len(open_trades), 1)
    
    stats = {
        'total_open_trades': len(open_trades),
        'total_recent_trades': len(recent_trades),
        'total_open_pnl': round(total_open_pnl, 2),
        'total_margin_used': round(total_margin_used, 2),
        'avg_confidence': avg_confidence,
        'account_equity': round(sum(trade['equity'] for trade in open_trades) / len(open_trades), 2)
    }
    
    return render_template('dashboard.html', 
                         open_trades=open_trades, 
                         recent_trades=recent_trades,
                         stats=stats)

@app.route('/api')
@app.route('/drew/api')
def api_data():
    """JSON API endpoint"""
    open_trades, recent_trades = generate_trade_data()
    
    return jsonify({
        'timestamp': datetime.now().isoformat(),
        'open_trades': open_trades,
        'recent_trades': recent_trades,
        'summary': {
            'total_open_trades': len(open_trades),
            'total_recent_trades': len(recent_trades),
            'total_open_pnl': round(sum(trade['pnl'] for trade in open_trades), 2),
            'total_margin_used': round(sum(trade['margin_used'] for trade in open_trades), 2),
            'avg_confidence': round(sum(trade['confidence_score'] for trade in open_trades) / len(open_trades), 1)
        }
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=debug, host='0.0.0.0', port=port)