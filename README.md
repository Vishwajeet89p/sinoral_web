# SINORAL - Modern Company Website

A professional Flask-based website for SINORAL company with modern design and responsive layout.

## Features

- **Modern Design**: Clean, professional interface with gradient backgrounds
- **Responsive**: Works perfectly on desktop, tablet, and mobile devices
- **Flask Backend**: Python Flask framework for dynamic content
- **Contact Form**: Functional contact form with server-side processing
- **SEO Optimized**: Proper meta tags and semantic HTML structure
- **Fast Loading**: Optimized CSS and JavaScript

## Project Structure

```
sinoral-website/
├── main.py              # Flask application entry point
├── startup.py           # Alternative startup script
├── requirements.txt     # Python dependencies
├── web.config          # Azure App Service configuration
├── templates/          # Jinja2 HTML templates
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── services.html
│   ├── contact.html
│   ├── 404.html
│   └── 500.html
└── static/             # Static assets
    ├── css/
    │   └── style.css
    ├── js/
    │   └── app.js
    └── images/         # For future image uploads
```

## Local Development

1. Install Python 3.7+ and create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python main.py
```

4. Open your browser and visit: `http://localhost:5000`

## Deployment to Azure App Service

### Method 1: FTP Deployment
1. Create all files in your local directory
2. Connect to Azure App Service FTP using credentials from Azure Portal
3. Upload all files to `/site/wwwroot/` directory
4. Ensure `main.py` is in the root directory
5. Azure will automatically detect and run the Flask app

### Method 2: ZIP Deployment
1. Create a ZIP file with all project files
2. Use Azure Portal or Azure CLI to deploy:
```bash
az webapp deployment source config-zip --resource-group <resource-group> --name <app-name> --src <zip-file>
```

### Method 3: Git Deployment
1. Initialize git repository and push to Azure or GitHub
2. Configure continuous deployment in Azure Portal
3. Azure will automatically build and deploy

## Configuration for Azure

The application is configured to work with Azure App Service:
- `web.config`: Configuration for Windows-based App Service
- `startup.py`: Alternative entry point if needed
- `PORT` environment variable handling for Azure hosting
- Static files properly configured for Azure serving

## Customization

### Company Information
Edit the following in templates:
- Company name: Search for "SINORAL" in templates
- Contact information: Update in `templates/contact.html` and `templates/base.html`
- Services: Modify the services array in `main.py`

### Styling
- Colors and themes: Edit CSS variables in `static/css/style.css`
- Layout: Modify HTML templates in `templates/` directory
- Animations: Update JavaScript in `static/js/app.js`

### Adding New Pages
1. Create new route in `main.py`
2. Create corresponding HTML template in `templates/`
3. Add navigation link in `templates/base.html`

## Browser Support

- Chrome 60+
- Firefox 60+
- Safari 12+
- Edge 79+
- Internet Explorer 11+ (limited)

## License

This project is created for SINORAL company. All rights reserved.
