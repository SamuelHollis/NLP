def index():
    prediction_text = None
    if request.method == "POST":
        # Obtener la URL del formulario
        user_url = request.form["url"]
        
        # Procesar la URL (aquí debes incluir cualquier procesamiento necesario que usaste al entrenar tu modelo)
        # Por ejemplo, transformar la URL en una representación adecuada para el modelo
        # input_data = transform(user_url) # Esta es solo una indicación de lo que podrías hacer
        
        # Realizar la predicción
        prediction = model.predict([user_url])[0]
        
        # Determinar el resultado
        prediction_text = 'Spam' if prediction == 1 else 'Not Spam'
    
    return render_template("index.html", prediction=prediction_text)
