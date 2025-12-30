# Django Tools

A comprehensive Django web application that provides utility tools including a password generator and real-time weather information. Built with Django, Tailwind CSS, and modern web technologies.

## Features

- **Password Generator**: Create strong, customizable passwords with options for:
  - Adjustable length (6-16 characters)
  - Uppercase letters
  - Digits
  - Special symbols

- **Weather Information**: Get real-time weather data for any city worldwide with:
  - Current temperature and conditions
  - Humidity, pressure, wind speed, and visibility
  - Support for multiple temperature units (Celsius, Fahrenheit, Kelvin)
  - Beautiful, responsive UI with weather icons

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- Node.js 16 or higher
- npm or yarn
- Git

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/NjauSamuel/Django-Password-Generator.git
   cd Django-Password-Generator
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Python dependencies**
   ```bash
   pip install django python-dotenv requests
   ```

5. **Install Node.js dependencies**
   ```bash
   npm install
   ```

6. **Build the frontend assets**
   ```bash
   npm run build
   ```

## Getting Your OpenWeather API Key

The weather feature requires an API key from OpenWeatherMap. Follow these steps to obtain one:

### Step 1: Create an Account

1. Visit [OpenWeatherMap](https://openweathermap.org/)
2. Click on **"Sign Up"** in the top right corner
3. Fill in your account details:
   - Username
   - Email address
   - Password
   - First and Last name
4. Accept the terms of service and privacy policy
5. Click **"Create Account"**

### Step 2: Verify Your Email

1. Check your email inbox for a verification email from OpenWeatherMap
2. Click the verification link in the email
3. You'll be redirected to a confirmation page

### Step 3: Get Your API Key

1. After logging in, navigate to the [API Keys page](https://home.openweathermap.org/api_keys)
2. You'll see a default API key named "Default" (or you can create a new one)
3. **Important**: The API key may take a few minutes to activate (usually 10-60 minutes)
4. Copy your API key - you'll need it in the next step

### Step 4: Configure Your API Key

1. In the project root directory, create a `.env` file:
   ```bash
   touch .env
   ```

2. Add your OpenWeather API key to the `.env` file:
   ```
   OPENWEATHER_API_KEY=your_api_key_here
   ```

   Replace `your_api_key_here` with the actual API key you copied from OpenWeatherMap.

3. **Important**: The `.env` file is already in `.gitignore`, so your API key won't be committed to version control.


## Configuration

### Environment Variables

Create a `.env` file in the project root with the following variables:

```env
OPENWEATHER_API_KEY=your_openweather_api_key_here
```

### Django Settings

The application uses Django's default settings. Key configurations:

- **Static Files**: Located in `static/` directory
- **Templates**: Located in each app's `templates/` directory
- **Database**: SQLite (default, can be changed in `mysite/settings.py`)

## Running the Application

1. **Build frontend assets** (if you haven't already):
   ```bash
   npm run build
   ```

   Or run in watch mode for development:
   ```bash
   npm run dev
   ```

2. **Run database migrations**:
   ```bash
   python manage.py migrate
   ```

3. **Start the Django development server**:
   ```bash
   python manage.py runserver
   ```

4. **Access the application**:
   - Open your browser and navigate to `http://127.0.0.1:8000/`
   - You should see the Django Tools homepage


## Technologies Used

- **Backend**:
  - Django 6.0
  - Python 3.8+
  - python-dotenv (for environment variables)
  - requests (for API calls)

- **Frontend**:
  - Tailwind CSS 4.1
  - Vite 7.3
  - Modern HTML5/CSS3

- **APIs**:
  - OpenWeatherMap API (for weather data)

## Development

### Frontend Development

To watch for changes and automatically rebuild CSS:

```bash
npm run dev
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the ISC License.

## Author

NjauSamuel

## Support

For issues or questions:
- Open an issue on [GitHub](https://github.com/NjauSamuel/Django-Password-Generator/issues)
- Check the [OpenWeatherMap API documentation](https://openweathermap.org/api) for API-related questions
