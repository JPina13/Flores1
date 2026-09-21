from flask import Flask, render_template_string

app = Flask(__name__)

HTML = r"""
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Flores amarillas para ti 💛</title>

<style>

*{
    box-sizing:border-box;
}

body{
    margin:0;
    min-height:100vh;
    font-family:"Segoe UI", sans-serif;
    background:
        radial-gradient(circle at 50% 20%, #fffef2 0%, #fff8c9 45%, #ffeaa0 100%);
    overflow-x:hidden;
    color:#624b12;
}

/* =========================
   CONTENEDOR
========================= */

.page{
    min-height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    padding:30px 15px;
}

.card{
    width:min(94vw, 520px);
    text-align:center;
    padding:30px 20px 35px;

    background:rgba(255,255,255,.42);
    border:1px solid rgba(255,255,255,.7);
    border-radius:30px;

    box-shadow:
        0 20px 60px rgba(126,94,0,.15);

    backdrop-filter:blur(7px);

    position:relative;
    z-index:5;
}

h1{
    margin:0;
    font-size:clamp(2rem,7vw,3rem);
    color:#c58c00;
}

.subtitle{
    margin:10px auto 0;
    max-width:380px;
    line-height:1.5;
    font-size:1.08rem;
}


/* =========================
   RAMO
========================= */

.bouquet{
    position:relative;
    width:360px;
    height:390px;

    max-width:100%;

    margin:10px auto 0;
}


/* =========================
   TALLOS
========================= */

.stem{

    position:absolute;

    width:9px;
    height:240px;

    background:
        linear-gradient(
            90deg,
            #376b29,
            #65a84a,
            #356827
        );

    border-radius:10px;

    transform-origin:bottom;

    bottom:35px;
    left:50%;

    z-index:1;
}


/* tallos individuales */

.s1{
    transform:translateX(-50%) rotate(-18deg);
}

.s2{
    transform:translateX(-50%) rotate(18deg);
}

.s3{
    height:270px;
    transform:translateX(-50%);
}

.s4{
    height:215px;
    transform:translateX(-50%) rotate(-9deg);
}

.s5{
    height:215px;
    transform:translateX(-50%) rotate(10deg);
}


/* =========================
   HOJAS
========================= */

.leaf{

    position:absolute;

    width:70px;
    height:36px;

    background:
        linear-gradient(
            135deg,
            #5b9c45,
            #34722d
        );

    border-radius:
        100% 0
        100% 0;

    z-index:2;
}

.leaf1{
    left:90px;
    bottom:120px;
    transform:rotate(20deg);
}

.leaf2{
    right:85px;
    bottom:135px;
    transform:scaleX(-1) rotate(25deg);
}

.leaf3{
    left:125px;
    bottom:80px;
    transform:rotate(-15deg);
}

.leaf4{
    right:125px;
    bottom:85px;
    transform:scaleX(-1) rotate(-15deg);
}


/* =========================
   GIRASOLES
========================= */

.sunflower{

    --size:120px;

    position:absolute;

    width:var(--size);
    height:var(--size);

    z-index:4;

    animation:
        flowerMovement
        4s
        ease-in-out
        infinite;

}


/* posiciones */

.flower1{

    --size:135px;

    left:112px;
    top:45px;

    z-index:7;
}


.flower2{

    --size:115px;

    left:35px;
    top:115px;

    transform:rotate(-10deg);

    animation-delay:.4s;

}


.flower3{

    --size:110px;

    right:30px;
    top:120px;

    transform:rotate(12deg);

    animation-delay:.8s;
}


.flower4{

    --size:95px;

    left:75px;
    top:210px;

    animation-delay:1.2s;

}


.flower5{

    --size:95px;

    right:72px;
    top:210px;

    animation-delay:1.5s;

}


/* =========================
   PÉTALOS
========================= */

.petal{

    position:absolute;

    left:50%;
    top:50%;

    width:22%;
    height:47%;

    transform-origin:
        50%
        100%;

    border-radius:
        60% 60%
        45% 45%;

    background:

        linear-gradient(
            to bottom,
            #ffe347,
            #ffc400 65%,
            #eda900
        );

    box-shadow:

        inset 0 -5px 7px
        rgba(184,121,0,.12);

}


/*
Los pétalos se generan alrededor
del centro usando rotaciones.
*/

.p1  {transform:translate(-50%,-100%) rotate(0deg);}
.p2  {transform:translate(-50%,-100%) rotate(20deg);}
.p3  {transform:translate(-50%,-100%) rotate(40deg);}
.p4  {transform:translate(-50%,-100%) rotate(60deg);}
.p5  {transform:translate(-50%,-100%) rotate(80deg);}
.p6  {transform:translate(-50%,-100%) rotate(100deg);}
.p7  {transform:translate(-50%,-100%) rotate(120deg);}
.p8  {transform:translate(-50%,-100%) rotate(140deg);}
.p9  {transform:translate(-50%,-100%) rotate(160deg);}
.p10 {transform:translate(-50%,-100%) rotate(180deg);}
.p11 {transform:translate(-50%,-100%) rotate(200deg);}
.p12 {transform:translate(-50%,-100%) rotate(220deg);}
.p13 {transform:translate(-50%,-100%) rotate(240deg);}
.p14 {transform:translate(-50%,-100%) rotate(260deg);}
.p15 {transform:translate(-50%,-100%) rotate(280deg);}
.p16 {transform:translate(-50%,-100%) rotate(300deg);}
.p17 {transform:translate(-50%,-100%) rotate(320deg);}
.p18 {transform:translate(-50%,-100%) rotate(340deg);}


/* =========================
   CENTRO GIRASOL
========================= */

.flower-center{

    position:absolute;

    width:43%;
    height:43%;

    left:28.5%;
    top:28.5%;

    border-radius:50%;

    z-index:10;

    background:

        radial-gradient(
            circle at 35% 35%,
            #8e650d 0%,
            #684500 30%,
            #3c2700 65%,
            #281900 100%
        );

    box-shadow:

        inset 0 0 10px
        rgba(0,0,0,.35),

        0 2px 5px
        rgba(0,0,0,.15);

}


/* textura semillas */

.flower-center::after{

    content:"";

    position:absolute;

    inset:8%;

    border-radius:50%;

    opacity:.45;

    background-image:

        radial-gradient(
            #e4ad2b 1px,
            transparent 1.5px
        );

    background-size:6px 6px;

}


/* =========================
   PAPEL DEL RAMO
========================= */

.paper{

    position:absolute;

    left:50%;
    bottom:5px;

    transform:
        translateX(-50%);

    width:180px;
    height:135px;

    background:

        linear-gradient(
            135deg,
            #e5bd7b,
            #c9954f
        );

    clip-path:

        polygon(
            5% 0,
            95% 0,
            67% 100%,
            33% 100%
        );

    z-index:3;

    opacity:.95;

}


.ribbon{

    position:absolute;

    left:50%;
    bottom:42px;

    transform:
        translateX(-50%);

    width:75px;
    height:16px;

    background:#e6aa00;

    border-radius:20px;

    z-index:8;

    box-shadow:
        0 3px 6px
        rgba(100,60,0,.2);

}


/* =========================
   BOTÓN
========================= */

button{

    border:0;

    padding:
        13px 24px;

    border-radius:30px;

    background:
        linear-gradient(
            135deg,
            #f4bd00,
            #d99800
        );

    color:white;

    font-weight:600;

    font-size:1rem;

    cursor:pointer;

    box-shadow:
        0 8px 20px
        rgba(192,137,0,.25);

    transition:
        transform .2s,
        box-shadow .2s;

}

button:hover{

    transform:
        translateY(-2px);

    box-shadow:
        0 12px 25px
        rgba(192,137,0,.35);

}


/* =========================
   MENSAJE
========================= */

#specialMessage{

    display:none;

    max-width:390px;

    margin:
        20px auto 0;

    padding:17px;

    background:
        rgba(255,250,214,.8);

    border-radius:18px;

    line-height:1.6;

    animation:
        showMessage
        .8s ease;

}


/* =========================
   PÉTALOS CAYENDO
========================= */

.fallingPetal{

    position:fixed;

    top:-30px;

    width:13px;
    height:20px;

    background:#ffd52c;

    border-radius:
        100% 0
        100% 0;

    pointer-events:none;

    z-index:1;

    animation:
        falling
        linear
        infinite;

}


/* =========================
   ANIMACIONES
========================= */

@keyframes flowerMovement{

    0%,100%{
        translate:0 0;
        rotate:-1deg;
    }

    50%{
        translate:0 -3px;
        rotate:2deg;
    }

}


@keyframes falling{

    0%{

        transform:
            translateY(-30px)
            translateX(0)
            rotate(0);

    }

    50%{

        transform:
            translateY(50vh)
            translateX(35px)
            rotate(180deg);

    }

    100%{

        transform:
            translateY(110vh)
            translateX(-25px)
            rotate(420deg);

    }

}


@keyframes showMessage{

    from{
        opacity:0;
        transform:
            translateY(15px);
    }

    to{
        opacity:1;
        transform:
            translateY(0);
    }

}


/* =========================
   CELULAR
========================= */

@media(max-width:480px){

    .card{

        padding:
            25px 12px
            30px;

    }

    .bouquet{

        transform:
            scale(.88);

        margin-top:-5px;
        margin-bottom:-20px;

    }

}

</style>

</head>


<body>

<div id="petalContainer"></div>


<div class="page">

<div class="card">

<h1>
Flores amarillas para ti 💛
</h1>

<p class="subtitle">
Porque hay personas que hacen que un día cualquiera
se sienta un poquito más bonito.
</p>


<div class="bouquet">


<!-- TALLOS -->

<div class="stem s1"></div>
<div class="stem s2"></div>
<div class="stem s3"></div>
<div class="stem s4"></div>
<div class="stem s5"></div>


<!-- HOJAS -->

<div class="leaf leaf1"></div>
<div class="leaf leaf2"></div>
<div class="leaf leaf3"></div>
<div class="leaf leaf4"></div>


<!-- GIRASOL 1 -->

<div class="sunflower flower1">

<div class="petal p1"></div>
<div class="petal p2"></div>
<div class="petal p3"></div>
<div class="petal p4"></div>
<div class="petal p5"></div>
<div class="petal p6"></div>
<div class="petal p7"></div>
<div class="petal p8"></div>
<div class="petal p9"></div>
<div class="petal p10"></div>
<div class="petal p11"></div>
<div class="petal p12"></div>
<div class="petal p13"></div>
<div class="petal p14"></div>
<div class="petal p15"></div>
<div class="petal p16"></div>
<div class="petal p17"></div>
<div class="petal p18"></div>

<div class="flower-center"></div>

</div>


<!-- GIRASOLES GENERADOS POR JS -->

<div
class="sunflower flower2 generated">
</div>

<div
class="sunflower flower3 generated">
</div>

<div
class="sunflower flower4 generated">
</div>

<div
class="sunflower flower5 generated">
</div>


<!-- PAPEL -->

<div class="paper"></div>

<div class="ribbon"></div>

</div>


<button onclick="showMessage()">

Tengo algo que decirte 💛

</button>


<div id="specialMessage">

🌻 Estas flores no se marchitan,
así que puedes quedártelas todo el tiempo que quieras.

<br><br>

Solo quería tener un pequeño detalle contigo
y recordarte que alguien pensó en ti hoy. 💛

</div>


</div>

</div>


<script>

/* =====================================
   CREAR PÉTALOS DE LOS OTROS GIRASOLES
===================================== */

const generatedFlowers =
document.querySelectorAll(
    ".generated"
);


generatedFlowers.forEach(
flower => {

    for(
        let i = 1;
        i <= 18;
        i++
    ){

        const petal =
        document.createElement(
            "div"
        );

        petal.className =
        "petal p" + i;

        flower.appendChild(
            petal
        );

    }


    const center =
    document.createElement(
        "div"
    );

    center.className =
    "flower-center";

    flower.appendChild(
        center
    );

});


/* =====================================
   PÉTALOS CAYENDO
===================================== */

const container =
document.getElementById(
    "petalContainer"
);


for(
    let i = 0;
    i < 20;
    i++
){

    const petal =
    document.createElement(
        "div"
    );

    petal.className =
    "fallingPetal";


    petal.style.left =
    Math.random() * 100
    + "vw";


    petal.style.animationDuration =
    (
        7 +
        Math.random() * 7
    )
    + "s";


    petal.style.animationDelay =
    (
        -Math.random() * 12
    )
    + "s";


    petal.style.opacity =
    .35 +
    Math.random() * .55;


    const size =
    8 +
    Math.random() * 9;


    petal.style.width =
    size + "px";


    petal.style.height =
    size * 1.5 + "px";


    container.appendChild(
        petal
    );

}


/* =====================================
   MENSAJE
===================================== */

function showMessage(){

    const message =
    document.getElementById(
        "specialMessage"
    );

    message.style.display =
    "block";


    setTimeout(
        () => {

            message.scrollIntoView({
                behavior:"smooth",
                block:"center"
            });

        },
        100
    );

}

</script>


</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )
