import logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    logging.debug("Rendering index.html template.")
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    logging.debug("Rendering result.html template.")
    try:
        # Your prediction logic here
        pass
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return render_template('result.html', error=str(e))
