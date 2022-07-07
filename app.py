from pycaret.regression import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np

model = load_model('pickle_model')

def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Class'][0]
    return predictions

def run():

    from PIL import Image

    st.title("App de prediccion de divorcios")
   
    Atr1 = st.number_input('Si uno de nosotros se disculpa cuando nuestra discusión se deteriora, la discusión termina.', min_value=0, max_value=4, value=0)
    Atr2 = st.number_input('Sé que podemos ignorar nuestras diferencias, incluso si las cosas se ponen difíciles a veces.', min_value=0, max_value=4, value=0)
    Atr3 = st.number_input('Cuando lo necesitemos, podemos tomar nuestras conversaciones con mi cónyuge desde el principio y corregirlo.', min_value=0, max_value=4, value=0)
    Atr4 = st.number_input('Cuando discuto con mi cónyuge, contactarlo eventualmente funcionará.', min_value=0, max_value=4, value=0)
    Atr5 = st.number_input('El tiempo que pasé con mi esposa es especial para nosotros.', min_value=0, max_value=4, value=0)
    Atr6 = st.number_input('No tenemos tiempo en casa como pareja.', min_value=0, max_value=4, value=0)
    Atr7 = st.number_input('Somos como dos extraños que comparten el mismo ambiente en el hogar en lugar de la familia.', min_value=0, max_value=4, value=0)
    Atr8 = st.number_input('Disfruto de nuestras vacaciones con mi esposa.', min_value=0, max_value=4, value=0)
    Atr9 = st.number_input('Disfruto viajar con mi esposa.', min_value=0, max_value=4, value=0)
    Atr10 = st.number_input('La mayoría de nuestras metas son comunes a mi cónyuge.', min_value=0, max_value=4, value=0)
    Atr11 = st.number_input('Creo que algún día en el futuro, cuando miro hacia atrás, veo que mi cónyuge y yo hemos estado en armonía el uno con el otro.', min_value=0, max_value=4, value=0)
    Atr12 = st.number_input('Mi cónyuge y yo tenemos valores similares en términos de libertad personal.', min_value=0, max_value=4, value=0)
    Atr13 = st.number_input('Mi cónyuge y yo tenemos un sentido similar del entretenimiento.', min_value=0, max_value=4, value=0)
    Atr14 = st.number_input('¿La mayoría de nuestras metas para las personas (hijos, amigos, etc., son las mismas?', min_value=0, max_value=4, value=0)
    Atr15 = st.number_input('¿Nuestros sueños con mi cónyuge son similares y armoniosos?', min_value=0, max_value=4, value=0)
    Atr16 = st.number_input('¿Somos compatibles con mi cónyuge sobre lo que debe ser el amor?', min_value=0, max_value=4, value=0)
    Atr17 = st.number_input('¿Compartimos los mismos puntos de vista sobre ser felices en nuestra vida con mi cónyuge?', min_value=0, max_value=4, value=0)
    Atr18 = st.number_input('¿Mi cónyuge y yo tenemos ideas similares sobre cómo debe ser el matrimonio?', min_value=0, max_value=4, value=0)
    Atr19 = st.number_input('¿Mi cónyuge y yo tenemos ideas similares sobre cómo deben ser los roles en el matrimonio?', min_value=0, max_value=4, value=0)
    Atr20 = st.number_input('¿Mi cónyuge y yo tenemos valores similares en confianza?', min_value=0, max_value=4, value=0)
    Atr21 = st.number_input('¿Sé exactamente lo que le gusta a mi esposa(o)?', min_value=0, max_value=4, value=0)
    Atr22 = st.number_input('¿Sé cómo quiere que lo cuiden mi cónyuge cuando está enfermo?', min_value=0, max_value=4, value=0)
    Atr23 = st.number_input('¿Sé cuál es la comida favorita de mi cónyuge?', min_value=0, max_value=4, value=0)
    Atr24 = st.number_input('¿Puedo decirle qué tipo de estrés enfrenta mi cónyuge en su vida?', min_value=0, max_value=4, value=0)
    Atr25 = st.number_input('¿Tengo conocimiento del mundo interior de mi cónyuge?', min_value=0, max_value=4, value=0)
    Atr26 = st.number_input('¿Conozco las ansiedades básicas de mi cónyuge.?', min_value=0, max_value=4, value=0)
    Atr27 = st.number_input('¿Sé cuáles son las fuentes actuales de estrés de mi cónyuge.?', min_value=0, max_value=4, value=0)
    Atr28 = st.number_input('¿Conozco las esperanzas y los deseos de mi cónyuge.?', min_value=0, max_value=4, value=0)
    Atr29 = st.number_input('¿Conozco muy bien a mi cónyuge.?', min_value=0, max_value=4, value=0)
    Atr30 = st.number_input('¿Conozco a los amigos de mi cónyuge y sus relaciones sociales?', min_value=0, max_value=4, value=0)
    Atr31 = st.number_input('¿Me siento agresivo cuando discuto con mi cónyuge.?', min_value=0, max_value=4, value=0)
    Atr32 = st.number_input('¿Cuando discuto con mi pareja, suelo usar expresiones como "tú siempre" o "tú nunca".?', min_value=0, max_value=4, value=0)
    Atr33 = st.number_input('Puedo usar declaraciones negativas sobre la personalidad de mi cónyuge durante nuestras conversaciones.?', min_value=0, max_value=4, value=0)
    Atr34 = st.number_input('Puedo usar expresiones ofensivas durante nuestras discusiones.?', min_value=0, max_value=4, value=0)
    Atr35 = st.number_input('Puedo insultar a mi cónyuge durante nuestras discusiones.', min_value=0, max_value=4, value=0)
    Atr36 = st.number_input('Puede ser humillante cuando discutimos.', min_value=0, max_value=4, value=0)
    Atr37 = st.number_input('Mi discusión con mi cónyuge no es tranquila.', min_value=0, max_value=4, value=0)
    Atr38 = st.number_input('Odio la forma en que mi cónyuge abre un tema.', min_value=0, max_value=4, value=0)
    Atr39 = st.number_input('¿Nuestras discusiones a menudo ocurren repentinamente.?', min_value=0, max_value=4, value=0)
    Atr40 = st.number_input('¿Estamos empezando una discusión antes de que sepa lo que está pasando.?', min_value=0, max_value=4, value=0)
    Atr41 = st.number_input('¿Cuando hablo con mi cónyuge sobre algo, mi calma se rompe repentinamente.?', min_value=0, max_value=4, value=0)
    Atr42 = st.number_input('¿Cuando discuto con mi pareja, solo salgo y no digo una palabra.?', min_value=0, max_value=4, value=0)
    Atr43 = st.number_input('¿Mayormente me quedo en silencio para calmar un poco el ambiente.?', min_value=0, max_value=4, value=0)
    Atr44 = st.number_input('¿A veces pienso que es bueno para mí salir de casa por un tiempo.?', min_value=0, max_value=4, value=0)
    Atr45 = st.number_input('¿Prefiero quedarme en silencio que discutir con mi cónyuge.?', min_value=0, max_value=4, value=0)
    Atr46 = st.number_input('¿Incluso si tengo razón en la discusión, me quedo en silencio para lastimar a mi cónyuge.?', min_value=0, max_value=4, value=0)
    Atr47 = st.number_input('¿Cuando discuto con mi cónyuge, me quedo en silencio porque tengo miedo de no poder controlar mi ira.?', min_value=0, max_value=4, value=0)
    Atr48 = st.number_input('¿Me siento bien en nuestras discusiones.?', min_value=0, max_value=4, value=0)
    Atr49 = st.number_input('¿No tengo nada que ver con lo que se me acusa.?', min_value=0, max_value=4, value=0)
    Atr50 = st.number_input('¿En realidad no soy yo el culpable de lo que se me acusa.?', min_value=0, max_value=4, value=0)
    Atr51 = st.number_input('¿ No soy yo el que se equivoca con los problemas en casa.?', min_value=0, max_value=4, value=0)
    Atr52 = st.number_input('¿No dudaría en decirle a mi cónyuge sobre su insuficiencia?', min_value=0, max_value=4, value=0)
    Atr53 = st.number_input('¿Cuando discuto, le recuerdo a mi cónyuge su insuficiencia?', min_value=0, max_value=4, value=0)
    Atr54 = st.number_input('¿No tengo miedo de decirle a mi cónyuge sobre su incompetencia?', min_value=0, max_value=4, value=0)
    output=""

    input_dict = {'Atr1' : Atr1, 'Atr2' : Atr2, 'Atr3' : Atr3,  'Atr4' : Atr4, 'Atr5' : Atr5, 'Atr6' : Atr6, 'Atr7' : Atr7, 'Atr8' : Atr8, 'Atr9' : Atr9, 'Atr10' : Atr10, 'Atr11' : Atr11, 'Atr12' : Atr12, 'Atr13' : Atr13,'Atr14' : Atr14, 'Atr15' : Atr15, 'Atr16' : Atr16, 'Atr17' : Atr17, 'Atr18' : Atr18, 'Atr19' : Atr19, 'Atr20' : Atr20, 'Atr21' : Atr21, 'Atr22' : Atr22, 'Atr23' : Atr23, 'Atr24' : Atr24, 'Atr25' : Atr25, 'Atr26' : Atr26, 'Atr27' : Atr27, 'Atr28' : Atr28, 'Atr29' : Atr29, 'Atr30' : Atr30, 'Atr31' : Atr31, 'Atr32' : Atr32, 'Atr33' : Atr33, 'Atr34' : Atr34, 'Atr35' : Atr35, 'Atr36' : Atr36, 'Atr37' : Atr37, 'Atr38' : Atr38, 'Atr39' : Atr39, 'Atr40' : Atr40, 'Atr41' : Atr41,'Atr42' : Atr42, 'Atr43' : Atr43,'Atr44' : Atr44, 'Atr45' : Atr45,'Atr46' : Atr46, 'Atr47' : Atr47,'Atr48' : Atr48, 'Atr49' : Atr49,'Atr50' : Atr50, 'Atr51' : Atr51,'Atr52' : Atr52, 'Atr53' : Atr53,'Atr54' : Atr54}
    input_df = pd.DataFrame([input_dict])

    if st.button("Predict"):
        output = predict(model=model, input_df=input_df)
        output = str(output)
        resultado=str(output)

    if resultado == 1 : 
        st.success('PREDICCION: DIVORCIO')
    else :
        st.success('PREDICCION: TERAPIA DE PAREJA')

    #st.success('The output is {}'.format(output))


if __name__ == '__main__':
    run()