from django.shortcuts import render

# Create your views here.



page = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Landing Page</title>

    <style>
@import url('https://fonts.googleapis.com/css2?family=Audiowide&family=Bungee&family=Cabin+Sketch&family=Fredericka+the+Great&family=Monoton&family=Nanum+Brush+Script&family=Nixie+One&family=Rubik+Bubbles&family=Rubik+Moonrocks&family=Rubik+Puddles&family=Source+Sans+Pro:ital,wght@0,200;0,300;0,400;0,600;0,700;0,900;1,200;1,300;1,400;1,600;1,700;1,900&family=Vast+Shadow&display=swap');



body{
    margin: 0;
    padding: 0;
    border: 0;
    box-sizing: border-box;
    font-family: 'Source Sans Pro', sans-serif;
    background: #2c0746;
}


.all{
    position: relative;
    text-align: center;
}


header{
    position: relative;
    height: 10px;
    background: #70f;
}


section{
    position: relative;
    padding: 30px;
}

footer{
    position: relative;
    height: 30px;
    background: #f70;
}



h1{
    /* font-family: 'Audiowide', cursive; */
    /* font-family: 'Bungee', cursive; */
    /* font-family: 'Cabin Sketch', cursive; */
    /* font-family: 'Fredericka the Great', cursive; */
    font-family: 'Monoton', cursive;
    font-family: 'Nanum Brush Script', cursive;
    /* font-family: 'Rubik Bubbles', cursive; */
    /* font-family: 'Rubik Puddles', cursive; */
    /* font-family: 'Vast Shadow', cursive; */
    /* font-family: 'Rubik Bubbles', cursive; */
    /* font-family: 'Rubik Moonrocks', cursive; */
    font-size: 200px;
    margin: 120px 0;
    line-height: 130px;
    color: #f07;

}

.note1{
    color: #f70;
    margin: 30px;

}

.cta1{
    font-weight: bold;
    font-size: 60px;
    font-family: 'Nixie One', cursive;
    color: #0f7;
    margin: 60px;
}




/* @media Media queries */

@media (min-width: 980px) {

}

@media (max-width: 980px) {
    h1{
        font-size: 130px;
        color: #f06;
    }
}

@media (max-width: 768px) {
    img{
        position: relative;
        width: 80%;
        margin: auto;
    }
    h1{
        font-size: 100px;
        color: #f05;
        line-height: 90px;
    }
    section{
        padding: 120px 0;
    }
}

@media (max-width: 480px) {

}
    </style>
</head>
<body>
    <div class="respo"></div>

    <div class="all">
        
        <header>
        </header>
        <section>

            <img src="https://idd.cl/portfolio/img/svg/logo-es.svg" alt="">
            <h1>Disoñando para ud.</h1>
            <p class="note1">(no, no estoy durmiendo)</p>

            <a class="cta1" href="https://idd.cl/portfolio">idd.cl</a>
        </section>

        <footer>

        </footer>
    </div>
</body>
</html>"""

from django.http import HttpResponse


def homePageView(request):
    return HttpResponse(page)