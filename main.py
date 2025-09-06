from flask import Flask, render_template, request, flash, redirect, url_for
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'sinoral-secret-key-2025'  # Change this in production

@app.route('/')
def home():
    """Homepage route"""
    return render_template('index.html')

@app.route('/about')
def about():
    """About page route"""
    return render_template('about.html')

@app.route('/services')
def services():
    """Services page route"""
    services_data = [
        {
            'name': 'Technology Solutions',
            'description': 'Cutting-edge technology solutions for modern businesses',
            'icon': 'fas fa-laptop-code'
        },
        {
            'name': 'Digital Innovation', 
            'description': 'Innovative digital products and services',
            'icon': 'fas fa-lightbulb'
        },
        {
            'name': 'Consulting Services',
            'description': 'Expert consulting for digital transformation',
            'icon': 'fas fa-handshake'
        }
    ]
    return render_template('services.html', services=services_data)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page route with form handling"""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        if name and email and message:
            # In production, you would save to database or send email
            flash('Thank you for your message! We will get back to you soon.', 'success')
            return redirect(url_for('contact'))
        else:
            flash('Please fill in all fields.', 'error')

    return render_template('contact.html')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    # For local development
    app.run(debug=True)
