#ML_Mini_Project.py 
import streamlit as st
import numpy as np
from skimage.io import imread
from skimage.transform import resize
import joblib
from PIL import Image
import streamlit.components.v1 as components
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner


import time
import requests

import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner



st.title('Crop Disease Detector')


st.markdown('Crop protection is a major concern not only in the Indian subcontinent but across the whole world. However many farmers in India loose a large share of their harvest due to not enough awareness about the crop diseases.This website is for the users to upload an image of the leaf of the infected crop. We predict the disease and describe it and provide necessary treatments and precautions ')

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_url_hello = "https://assets9.lottiefiles.com/packages/lf20_sgn7zslb.json"
lottie_url_download = "https://assets4.lottiefiles.com/private_files/lf30_t26law.json"
lottie_hello = load_lottieurl(lottie_url_hello)
st_lottie(lottie_hello, key="hello1")

st.title('Upload an image of the leaf below')
model = joblib.load(r"C:\Users\SARATH\OneDrive\Desktop\Project\CDD")
uploaded_file = st.file_uploader("Upload Image",type = 'jpg')

if uploaded_file is not None:
  img = Image.open(uploaded_file)
  st.image(img,caption = 'Uploaded image')
if st.button('PREDICT'):
      
      CATEGORIES = ['Corn Common Rust','Tomato Leaf Mold','Tomato Late Blight','Potato Late Blight','Potato Early Blight','Grape Black Rot','Apple Scab','Apple Black Rot']
      flat_data = []
      img = np.array(img)
      img_resized = resize(img,(150,150,3)) 
      flat_data.append(img_resized.flatten())
      flat_data = np.array(flat_data)
      y_out = model.predict(flat_data)
      y_out = CATEGORIES[y_out[0]]
      st.title(f'Predicted output:{y_out}')
      #q = model.predict_proba(flat_data)
      

      if y_out == 'Corn Common Rust':
            st.header("About The Disease:")
            st.subheader('Common corn rust, caused by the fungus Puccinia sorghi, is the most frequently occurring of the two primary rust diseases of corn in India. Common rust begins with lesions on leaves resembling flecks which develop into small tan spots. These lesions will be found on both the upper and lower surfaces of the leaves or leaf sheaths and are scattered across the leaf surface. The lesions are circular to elongate and may occur in clusters.')
            st.header("Treatment:")
            st.subheader('To reduce the incidence of corn rust, plant only corn that has resistance to the fungus. Resistance is either in the form of race-specific resistance or partial rust resistance. In either case, no sweet corn is completely resistant. If the corn begins to show symptoms of infection, immediately spray with a fungicide.')
            st.header("Pesticides To Be Used:")
            st.subheader('Numerous fungicides are available for rust control. Products containing mancozeb, pyraclostrobin, pyraclostrobin + metconazole, pyraclostrobin + fluxapyroxad, azoxystrobin + propiconazole, trifloxystrobin + prothioconazole can be used to control the disease.')
      if y_out == 'Tomato Leaf Mold':
            st.header("About The Disease:")
            st.subheader('Tomato leaf mold is a fungal disease that can develop when there are extended periods of leaf wetness and the relative humidity is high (greater than 85 percent). Due to this moisture requirement, the disease is seen primarily in hoophouses and greenhouses.Symptoms start as pale green to yellowish spots on upper leaf surfaces that turn a bright yellow. The spots merge as the disease progresses and the foliage then dies. ')
            st.header("Treatment:")
            st.subheader('An apple-cider and vinegar mix is believed to treat the mold effectively. Corn and garlic spray can also be used to prevent fungi outbreaks before they even occur. There is also a milk-based spray that is touted as an all-natural, helpful cure for leaf mold.')
            st.header("Pesticides To Be Used:")
            st.subheader('Active ingredient chlorothalonil is the most recommended chemical for tomato leaf mold. It can be applied until the day before you pick tomatoes, which is a clear indication of its low toxicity.')
            
      if y_out == 'Tomato Late Blight':
            st.header("About The Disease:")
            st.subheader('Late blight is a potentially devastating disease of tomato, infecting leaves, stems and tomato fruit. The disease spreads quickly in fields and can result in total crop failure if untreated.Leaf symptoms of late blight first appear as small, water-soaked areas that rapidly enlarge to form purple-brown, oily-appearing blotches. On the lower side of leaves, rings of grayish white mycelium and spore-forming structures may appear around the blotches.')
            st.header("Treatment:")
            st.subheader('Use fungicide sprays based on mandipropamid, chlorothalonil, fluazinam, mancozeb to combat late blight. Fungicides are generally needed only if the disease appears during a time of year when rain is likely or overhead irrigation is practiced.')
            st.header("Pesticides To Be Used:")
            st.subheader('The severe late blight can be effectively managed with prophylactic spray of mancozeb at 0.25% followed by cymoxanil+mancozeb or dimethomorph+mancozeb at 0.3% at the onset of disease and one more spray of mancozeb at 0.25% seven days after application of systemic fungicides')
      if y_out == 'Potato Late Blight':
            st.header("About The Disease:")
            st.subheader('Initial symptoms of late blight are small, light to dark green, circular to irregular-shaped water-soaked spots. The first symptoms of late blight in the field are small, light to dark green, circular to irregular-shaped water-soaked spots. These lesions usually appear first on the lower leaves.')
            st.header("Treatment:")
            st.subheader('Late blight is controlled by eliminating cull piles and volunteer potatoes, using proper harvesting and storage practices, and applying fungicides when necessary. Air drainage to facilitate the drying of foliage each day is important.')
            st.header("Pesticides To Be Used:")
            st.subheader('One spray of mancozeb and latter two more sprays of translaminar/systemic + contact fungicides at 7–10 days interval give better results for managing late blight of potato')
      if y_out == 'Potato Early Blight':
            st.header("About The Disease:")
            st.subheader('Early blight is primarily a disease of stressed or senescing plants. Symptoms appear first on the oldest foliage. Affected leaves develop circular to angular dark brown lesions 0.12 to 0.16 inch (3–4 mm) in diameter. Concentric rings often form in lesions to produce characteristic target-board effect.Symptoms of early blight infection on tubers appear as dark and sunken lesions on the surface. Tuber lesions may be circular or irregular in shape and can be surrounded by a raised dark-brown border. The underlying tissue is dry with a corky texture and a dark-brown color ')
            st.header("Treatment:")
            st.subheader('Treatment of early blight includes prevention by planting potato varieties that are resistant to the disease.Avoid overhead irrigation and allow for sufficient aeration between plants to allow the foliage to dry as quickly as possible. Practice a 2-year crop rotation')
            st.header("Pesticides To Be Used:")
            st.subheader('Fungicides with protectant and curative properties are registered for use against early blight on potato. The cheaper protectant fungicides such as mancozeb and chlorothalonil are the foundation of most early blight management programs.')
      if y_out == 'Grape Black Rot':
            st.header("About The Disease:")
            st.subheader('Black rot, caused by the fungus Guignardia bidwellii, is a serious disease of cultivated and wild grapes. The disease is most destructive in warm, wet seasons. It attacks all green parts of the vine – leaves, shoots, leaf and fruit stems, tendrils, and fruit.Symptoms of black rot first appear as small yellowish spots on leaves. As the spots (lesions) enlarge, a dark border forms around the margins. The centers of the lesions become reddish brown. By the time the lesions reach 1/8 to 1/4 inch in diameter (approximately two weeks after infection), minute black dots appear.')    
            st.header("Treatment:")
            st.subheader('Make sure that all mummies have been removed from the vine and all plant material on the ground below is destroyed. Prune out any and all areas with lesions; grapevines can handle a severe pruning — when in doubt, cut it out.')
            st.header("Pesticides To Be Used:")
            st.subheader('Mancozeb, and Ziram are all highly effective against black rot. Because these fungicides are strictly protectants, they must be applied before the fungus infects or enters the plant. They protect fruit and foliage by preventing spore germination.')       
      if y_out == 'Apple Scab':
            st.header("About The Disease:")
            st.subheader('Apple scab produces dark blotches or lesions on the leaves, fruit, and sometimes young twigs. Infections in young leaves often cause leaf deformities, and affected plants may drop their fruit prematurely. All apple species (genus Malus) are affected, though some cultivars have greater resistance.Leaf spots are round, olive-green in color and up to ½-inch across. Spots are velvet-like with fringed borders. As they age, leaf spots turn dark brown to black, get bigger and grow together.')
            st.header("Treatment:")
            st.subheader('Apple Scab can be treated with: Propizol Fungicide (Crabapples only) or PHOSPHO-jet.Propizol is for ornamental use only. Fruit are not to be used for human or animal consumption.')
            st.header("Pesticides To Be Used:")
            st.subheader('Myclobutanil is a synthetic fungicide that is effective against apple scab. You can apply it any time from green tip until after petal fall.')
      if y_out == 'Apple Black Rot':
            st.header("About The Disease:")
            st.subheader('Black rot is caused by the fungus Diplodia seriata. The fungus can infect dead tissue as well as living trunks, branches, leaves and fruits. The black rot fungi survive Minnesota winters in branch cankers and mummified fruit (shriveled and dried fruit) attached to the tree.The earliest, most recognizable indicator of black rot infections are the leaf lesions. These appear as circular, tan lesions that have a darker margin. Within these lesions are small black spheres, or pycnidia.')
            st.header("Treatment:")
            st.subheader('Remove the cankers by pruning at least 15 inches below the end and burn or bury them. Also take preventative care with new season prunings and burn them, too.')
            st.header("Pesticides To Be Used:")
            st.subheader('Mancozeb, and Ziram are all highly effective against black rot. Because these fungicides are strictly protectants, they must be applied before the fungus infects or enters the plant. They protect fruit and foliage by preventing spore germination. They will not arrest lesion development after infection has occurred.')


#background-image: url('https://t4.ftcdn.net/jpg/04/16/21/59/360_F_416215928_QXQJPJE3wtgeOLmkBy0j0hemFZZgvt1B.jpg');
#background-image:url('https://media.istockphoto.com/photos/wood-texture-background-picture-id1045681578?b=1&k=20&m=1045681578&s=170667a&w=0&h=iwDsrcRJYE2W5fAa0YAF3LYR2mAMrAzezTRUkytWUhI=');

hide_st_style = """
            <style>
            #MainMenu {v
            # isibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

page_bg_img = '''
<style>
.css-1v3fvcr{

background-size: cover;

}


element.style {
    width: 100%;
    height: 100%;
    transform: translate3d(0px, 0px, 0px);
    content-visibility: visible;
    background-color: aqua;
}

svg[Attributes Style] {
    width: 512;
    height: 512;
}
user agent stylesheet
svg:not(:root) {
    overflow: hidden;
}
<style>
body {
    background-color: var(--background-color);
    color: var(--text-color);
}
<style>
:root {
    --primary-color: #ff4b4b;
    --background-color: #c88243f2;
    --secondary-background-color: #f0f2f6;
    --text-color: #31333F;
    --font: "Source Sans Pro", sans-serif;
}

h1{
    text-align:center;
}
img{
     position: relative;
    left: 273px;
}
p, ol, ul, dl {
    margin: 0px 0px 1rem;
    padding: 0px;
    font-size: 1rem;
    font-weight: 400;
    font-size: 20px;
    width: 968px;
    position: relative;
    left: -96px;
}
element.style {
    width: 100%;
    height: 100%;
    transform: translate3d(0px, 0px, 0px);
    content-visibility: visible;
    background-color: #c88243f2;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)