#!/usr/bin/env python3
import os
from main import app

if __name__ == "__main__":
    # Get port from environment variable (Azure sets this)
    port = int(os.environ.get('PORT', 5000))

    # Run the Flask app
    app.run(host='0.0.0.0', port=port, debug=False)
