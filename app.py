from flask import Flask, render_template_string

app = Flask(__name__)

HTML = r"""
<!DOCTYPE html>
<html lang="es">

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title>Flores amarillas para ti 💛</title>


<style>

/* ==============================
   GENERAL
============================== */

* {
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {

    margin: 0;

    min-height: 100vh;

    font-family:
        "Segoe UI",
        Arial,
        sans-serif;

    color: #624b12;

    background:
        radial-gradient(
            circle at 50% 20%,
            #fffef2 0%,
            #fff8c9 45%,
            #ffeaa0 100%
        );

    overflow-x: hidden;
}


/* ==============================
   PÁGINA
============================== */

.page {

    min-height: 100vh;

    display: flex;

    justify-content: center;

    align-items: center;

    padding: 30px 15px;
}


/* ==============================
   TARJETA
============================== */

.card {

    position: relative;

    z-index: 5;

    width: min(94vw, 520px);

    padding:
        30px
        20px
        35px;

    text-align: center;

    background:
        rgba(255,255,255,.48);

    border:
        1px solid
        rgba(255,255,255,.8);

    border-radius: 30px;

    box-shadow:
        0 20px 60px
        rgba(126,94,0,.15);

    backdrop-filter:
        blur(7px);
}


/* ==============================
   TÍTULO
============================== */

h1 {

    margin: 0;

    font-size:
        clamp(
            2rem,
            7vw,
            3rem
        );

    color: #c58c00;
}


.subtitle {

    max-width: 390px;

    margin:
        10px
        auto
        0;

    line-height: 1.55;

    font-size: 1.08rem;
}


/* ==============================
   RAMO
============================== */

.bouquet {

    position: relative;

    width: 360px;

    height: 390px;

    max-width: 100%;

    margin:
        10px
        auto
        0;
}


/* ==============================
   TALLOS
============================== */

.stem {

    position: absolute;

    left: 50%;

    bottom: 35px;

    width: 9px;

    height: 240px;

    z-index: 1;

    border-radius: 10px;

    transform-origin:
        bottom center;

    background:
        linear-gradient(
            90deg,
            #376b29,
            #65a84a,
            #356827
        );
}


.s1 {

    transform:
        translateX(-50%)
        rotate(-18deg);
}


.s2 {

    transform:
        translateX(-50%)
        rotate(18deg);
}


.s3 {

    height: 270px;

    transform:
        translateX(-50%);
}


.s4 {

    height: 215px;

    transform:
        translateX(-50%)
        rotate(-9deg);
}


.s5 {

    height: 215px;

    transform:
        translateX(-50%)
        rotate(10deg);
}


/* ==============================
   HOJAS
============================== */

.leaf {

    position: absolute;

    width: 70px;

    height: 36px;

    z-index: 2;

    border-radius:
        100%
        0
        100%
        0;

    background:
        linear-gradient(
            135deg,
            #69a64d,
            #34722d
        );

    box-shadow:
        inset
        -4px
        -4px
        7px
        rgba(0,0,0,.08);
}


.leaf1 {

    left: 90px;

    bottom: 120px;

    transform:
        rotate(20deg);
}


.leaf2 {

    right: 85px;

    bottom: 135px;

    transform:
        scaleX(-1)
        rotate(25deg);
}


.leaf3 {

    left: 125px;

    bottom: 80px;

    transform:
        rotate(-15deg);
}


.leaf4 {

    right: 125px;

    bottom: 85px;

    transform:
        scaleX(-1)
        rotate(-15deg);
}


/* ==============================
   GIRASOLES
============================== */

.sunflower {

    --size: 120px;

    position: absolute;

    width: var(--size);

    height: var(--size);

    z-index: 5;

    opacity: 0;

    scale: 0;

    cursor: pointer;

    user-select: none;

    touch-action: manipulation;

    -webkit-tap-highlight-color:
        transparent;

    transform-origin:
        50%
        60%;
}


/* Flor central */

.flower1 {

    --size: 135px;

    left: 112px;

    top: 42px;

    z-index: 9;

    animation:

        bloom
        1.1s
        cubic-bezier(.2,.9,.3,1.3)
        .4s
        forwards,

        flowerMovement
        4s
        ease-in-out
        1.5s
        infinite;
}


/* Flor izquierda */

.flower2 {

    --size: 115px;

    left: 35px;

    top: 120px;

    z-index: 7;

    animation:

        bloom
        1.1s
        cubic-bezier(.2,.9,.3,1.3)
        1s
        forwards,

        flowerMovement
        4.3s
        ease-in-out
        2.1s
        infinite;
}


/* Flor derecha */

.flower3 {

    --size: 110px;

    right: 30px;

    top: 120px;

    z-index: 7;

    animation:

        bloom
        1.1s
        cubic-bezier(.2,.9,.3,1.3)
        1.6s
        forwards,

        flowerMovement
        4.1s
        ease-in-out
        2.7s
        infinite;
}


/* Flor inferior izquierda */

.flower4 {

    --size: 95px;

    left: 75px;

    top: 210px;

    z-index: 6;

    animation:

        bloom
        1.1s
        cubic-bezier(.2,.9,.3,1.3)
        2.2s
        forwards,

        flowerMovement
        4.5s
        ease-in-out
        3.3s
        infinite;
}


/* Flor inferior derecha */

.flower5 {

    --size: 95px;

    right: 72px;

    top: 210px;

    z-index: 6;

    animation:

        bloom
        1.1s
        cubic-bezier(.2,.9,.3,1.3)
        2.8s
        forwards,

        flowerMovement
        4.2s
        ease-in-out
        3.9s
        infinite;
}


/* ==============================
   PÉTALOS
============================== */

.petal {

    position: absolute;

    left: 50%;

    top: 50%;

    width: 22%;

    height: 47%;

    transform-origin:
        50%
        100%;

    border-radius:
        60%
        60%
        45%
        45%;

    background:
        linear-gradient(
            to bottom,
            #ffe84e,
            #ffd014 45%,
            #f3ae00 100%
        );

    box-shadow:

        inset
        0
        -5px
        7px
        rgba(184,121,0,.12),

        0
        2px
        3px
        rgba(160,110,0,.08);
}


/* 18 pétalos */

.p1 {
    transform:
        translate(-50%,-100%)
        rotate(0deg);
}

.p2 {
    transform:
        translate(-50%,-100%)
        rotate(20deg);
}

.p3 {
    transform:
        translate(-50%,-100%)
        rotate(40deg);
}

.p4 {
    transform:
        translate(-50%,-100%)
        rotate(60deg);
}

.p5 {
    transform:
        translate(-50%,-100%)
        rotate(80deg);
}

.p6 {
    transform:
        translate(-50%,-100%)
        rotate(100deg);
}

.p7 {
    transform:
        translate(-50%,-100%)
        rotate(120deg);
}

.p8 {
    transform:
        translate(-50%,-100%)
        rotate(140deg);
}

.p9 {
    transform:
        translate(-50%,-100%)
        rotate(160deg);
}

.p10 {
    transform:
        translate(-50%,-100%)
        rotate(180deg);
}

.p11 {
    transform:
        translate(-50%,-100%)
        rotate(200deg);
}

.p12 {
    transform:
        translate(-50%,-100%)
        rotate(220deg);
}

.p13 {
    transform:
        translate(-50%,-100%)
        rotate(240deg);
}

.p14 {
    transform:
        translate(-50%,-100%)
        rotate(260deg);
}

.p15 {
    transform:
        translate(-50%,-100%)
        rotate(280deg);
}

.p16 {
    transform:
        translate(-50%,-100%)
        rotate(300deg);
}

.p17 {
    transform:
        translate(-50%,-100%)
        rotate(320deg);
}

.p18 {
    transform:
        translate(-50%,-100%)
        rotate(340deg);
}


/* ==============================
   CENTRO DE LA FLOR
============================== */

.flower-center {

    position: absolute;

    left: 28.5%;

    top: 28.5%;

    width: 43%;

    height: 43%;

    z-index: 10;

    border-radius: 50%;

    background:
        radial-gradient(
            circle at 35% 35%,
            #a77a16 0%,
            #755000 30%,
            #4a3000 65%,
            #281900 100%
        );

    box-shadow:

        inset
        0
        0
        10px
        rgba(0,0,0,.35),

        0
        2px
        5px
        rgba(0,0,0,.15);
}


/* Semillas */

.flower-center::after {

    content: "";

    position: absolute;

    inset: 8%;

    border-radius: 50%;

    opacity: .5;

    background-image:
        radial-gradient(
            #e5ad2b 1px,
            transparent 1.5px
        );

    background-size:
        6px
        6px;
}


/* ==============================
   PAPEL DEL RAMO
============================== */

.paper {

    position: absolute;

    left: 50%;

    bottom: 5px;

    width: 180px;

    height: 135px;

    z-index: 3;

    transform:
        translateX(-50%);

    background:
        linear-gradient(
            135deg,
            #e8c486,
            #c9944b
        );

    clip-path:
        polygon(
            5% 0,
            95% 0,
            67% 100%,
            33% 100%
        );

    opacity: .95;
}


.ribbon {

    position: absolute;

    left: 50%;

    bottom: 42px;

    width: 78px;

    height: 17px;

    z-index: 10;

    transform:
        translateX(-50%);

    border-radius: 20px;

    background:
        #e6aa00;

    box-shadow:
        0 3px 6px
        rgba(100,60,0,.2);
}


/* ==============================
   BOTÓN
============================== */

button {

    position: relative;

    z-index: 20;

    border: 0;

    padding:
        14px
        25px;

    border-radius: 30px;

    background:
        linear-gradient(
            135deg,
            #f4bd00,
            #dc9c00
        );

    color: white;

    font-size: 1rem;

    font-weight: 650;

    cursor: pointer;

    box-shadow:
        0 8px 20px
        rgba(192,137,0,.25);

    transition:
        transform .2s,
        box-shadow .2s;
}


button:hover {

    transform:
        translateY(-2px);

    box-shadow:
        0 12px 25px
        rgba(192,137,0,.35);
}


button:active {

    transform:
        scale(.96);
}


/* ==============================
   MENSAJE ESPECIAL
============================== */

#specialMessage {

    display: none;

    opacity: 0;

    max-width: 390px;

    margin:
        20px
        auto
        0;

    padding: 19px;

    line-height: 1.65;

    background:
        rgba(255,250,214,.9);

    border-radius: 18px;

    box-shadow:
        0 8px 25px
        rgba(150,110,0,.08);
}


/* Solo aparece cuando pulsamos botón */

#specialMessage.visible {

    display: block;

    animation:
        showMessage
        .8s
        ease
        forwards;
}


/* ==============================
   PÉTALOS DEL FONDO
============================== */

.fallingPetal {

    position: fixed;

    top: -30px;

    width: 13px;

    height: 20px;

    z-index: 1;

    pointer-events: none;

    border-radius:
        100%
        0
        100%
        0;

    background:
        #ffd52c;

    animation:
        falling
        linear
        infinite;
}


/* ==============================
   FLORECER
============================== */

@keyframes bloom {

    0% {

        opacity: 0;

        scale: 0;

        rotate: -15deg;
    }


    60% {

        opacity: 1;

        scale: 1.12;

        rotate: 4deg;
    }


    80% {

        scale: .95;

        rotate: -2deg;
    }


    100% {

        opacity: 1;

        scale: 1;

        rotate: 0deg;
    }
}


/* ==============================
   MOVIMIENTO NATURAL
============================== */

@keyframes flowerMovement {

    0%,
    100% {

        opacity: 1;

        scale: 1;

        translate:
            0
            0;

        rotate:
            -1deg;
    }


    50% {

        opacity: 1;

        scale: 1;

        translate:
            0
            -3px;

        rotate:
            2deg;
    }
}


/* ==============================
   CLICK EN FLOR
============================== */

.sunflower.clicked {

    opacity: 1 !important;

    animation:
        flowerClick
        .8s
        cubic-bezier(
            .34,
            1.56,
            .64,
            1
        )
        !important;
}


@keyframes flowerClick {

    0% {

        opacity: 1;

        scale: 1;

        rotate: 0deg;
    }


    20% {

        scale: 1.12;

        rotate: -9deg;
    }


    45% {

        scale: 1.18;

        rotate: 9deg;
    }


    70% {

        scale: 1.08;

        rotate: -4deg;
    }


    100% {

        opacity: 1;

        scale: 1;

        rotate: 0deg;
    }
}


/* Centro pulsa al tocar */

.sunflower.clicked
.flower-center {

    animation:
        centerPulse
        .8s
        ease-in-out;
}


@keyframes centerPulse {

    0%,
    100% {

        scale: 1;
    }


    50% {

        scale: 1.13;
    }
}


/* ==============================
   CAÍDA DE PÉTALOS
============================== */

@keyframes falling {

    0% {

        transform:
            translateY(-30px)
            translateX(0)
            rotate(0deg);
    }


    50% {

        transform:
            translateY(50vh)
            translateX(35px)
            rotate(180deg);
    }


    100% {

        transform:
            translateY(110vh)
            translateX(-25px)
            rotate(420deg);
    }
}


/* ==============================
   APARICIÓN MENSAJE
============================== */

@keyframes showMessage {

    from {

        opacity: 0;

        transform:
            translateY(15px)
            scale(.97);
    }


    to {

        opacity: 1;

        transform:
            translateY(0)
            scale(1);
    }
}


/* ==============================
   CELULAR
============================== */

@media(max-width:480px) {

    .page {

        padding:
            15px
            10px;
    }


    .card {

        padding:
            25px
            12px
            30px;
    }


    .bouquet {

        transform:
            scale(.88);

        margin-top:
            -5px;

        margin-bottom:
            -20px;
    }


    .subtitle {

        padding:
            0
            10px;
    }
}


/* ==============================
   ACCESIBILIDAD
============================== */

@media
(prefers-reduced-motion: reduce) {

    .sunflower,
    .fallingPetal {

        animation-duration:
            .01ms !important;

        animation-iteration-count:
            1 !important;

        opacity: 1;

        scale: 1;
    }
}

</style>

</head>


<body>


<!-- Pétalos flotantes -->

<div id="petalContainer"></div>


<div class="page">


<main class="card">


<h1>
    Flores amarillas para ti 💛
</h1>


<p class="subtitle">

    Adii, me dio pena pedir tu dirección para mandarte flores y probablemente hubiera sido una conversación muy sospechosa jajaja, asi que encontre otra manera.

</p>



<!-- ============================
     RAMO
============================ -->

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



<!-- FLOR CENTRAL -->

<div
    class="sunflower flower1"
    title="Tócame 🌻">
</div>


<!-- FLOR IZQUIERDA -->

<div
    class="sunflower flower2"
    title="Tócame 🌻">
</div>


<!-- FLOR DERECHA -->

<div
    class="sunflower flower3"
    title="Tócame 🌻">
</div>


<!-- FLOR INFERIOR IZQUIERDA -->

<div
    class="sunflower flower4"
    title="Tócame 🌻">
</div>


<!-- FLOR INFERIOR DERECHA -->

<div
    class="sunflower flower5"
    title="Tócame 🌻">
</div>



<!-- PAPEL -->

<div class="paper"></div>


<!-- CINTA -->

<div class="ribbon"></div>


</div>



<!-- ============================
     BOTÓN DEL MENSAJE
============================ -->

<button
    id="messageButton"
    type="button"
    onclick="showMessage()">

    Tengo algo que decirte 💛

</button>



<!-- ============================
     MENSAJE OCULTO
============================ -->

<div id="specialMessage">

    🌻 Estas flores no se marchitan,
    así que puedes quedártelas
    todo el tiempo que quieras.

    <br><br>

    Solo quería tener un pequeño
    detalle contigo y recordarte
    que alguien pensó en ti hoy. 💛

</div>


</main>

</div>



<script>


/* ==================================
   CREAR LOS GIRASOLES
================================== */

const flowers =
    document.querySelectorAll(
        ".sunflower"
    );


flowers.forEach(
    flower => {


        /* Crear 18 pétalos */

        for(
            let i = 1;
            i <= 18;
            i++
        ) {

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


        /* Crear centro */

        const center =
            document.createElement(
                "div"
            );


        center.className =
            "flower-center";


        flower.appendChild(
            center
        );

    }
);



/* ==================================
   PÉTALOS CAYENDO
================================== */

const petalContainer =
    document.getElementById(
        "petalContainer"
    );


for(
    let i = 0;
    i < 18;
    i++
) {

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
        (
            .30 +
            Math.random() * .50
        );


    const size =
        8 +
        Math.random() * 9;


    petal.style.width =
        size
        + "px";


    petal.style.height =
        (
            size * 1.5
        )
        + "px";


    petalContainer.appendChild(
        petal
    );
}



/* ==================================
   CLICK / TOUCH EN GIRASOLES
================================== */

flowers.forEach(
    flower => {


        flower.addEventListener(
            "click",
            function() {


                /*
                Reiniciar animación
                para poder tocarla
                varias veces
                */

                this.classList.remove(
                    "clicked"
                );


                void this.offsetWidth;


                this.classList.add(
                    "clicked"
                );


                /*
                Pequeña explosión
                de pétalos
                */

                createFlowerPetals(
                    this
                );


                /*
                Después regresamos
                a su movimiento normal
                */

                setTimeout(
                    () => {

                        this.classList.remove(
                            "clicked"
                        );

                    },
                    800
                );

            }
        );

    }
);



/* ==================================
   EXPLOSIÓN DE PÉTALOS
================================== */

function createFlowerPetals(
    flower
) {


    const rect =
        flower.getBoundingClientRect();


    const centerX =
        rect.left +
        rect.width / 2;


    const centerY =
        rect.top +
        rect.height / 2;


    for(
        let i = 0;
        i < 8;
        i++
    ) {


        const petal =
            document.createElement(
                "div"
            );


        petal.style.position =
            "fixed";


        petal.style.left =
            centerX
            + "px";


        petal.style.top =
            centerY
            + "px";


        petal.style.width =
            "10px";


        petal.style.height =
            "16px";


        petal.style.background =
            "linear-gradient(#ffe84e,#ffc400)";


        petal.style.borderRadius =
            "100% 0 100% 0";


        petal.style.pointerEvents =
            "none";


        petal.style.zIndex =
            "1000";


        document.body.appendChild(
            petal
        );


        const angle =
            Math.random()
            *
            Math.PI
            *
            2;


        const distance =
            40
            +
            Math.random()
            *
            60;


        const x =
            Math.cos(
                angle
            )
            *
            distance;


        const y =
            Math.sin(
                angle
            )
            *
            distance;


        const animation =
            petal.animate(

                [

                    {

                        transform:
                            "translate(-50%,-50%) rotate(0deg) scale(1)",

                        opacity: 1

                    },


                    {

                        transform:
                            `translate(
                                calc(-50% + ${x}px),
                                calc(-50% + ${y}px)
                            )
                            rotate(400deg)
                            scale(.5)`,

                        opacity: 0

                    }

                ],

                {

                    duration:
                        650
                        +
                        Math.random()
                        *
                        350,

                    easing:
                        "ease-out",

                    fill:
                        "forwards"

                }

            );


        animation.onfinish =
            () => {

                petal.remove();

            };

    }

}



/* ==================================
   MOSTRAR MENSAJE
================================== */

function showMessage() {


    const message =
        document.getElementById(
            "specialMessage"
        );


    const button =
        document.getElementById(
            "messageButton"
        );


    /*
    Si todavía está oculto,
    mostrarlo.
    */

    if(
        !message.classList.contains(
            "visible"
        )
    ) {


        message.classList.add(
            "visible"
        );


        /*
        Cambiar texto del botón
        */

        button.innerHTML =
            "Para ti 🌻";


        /*
        Llevar suavemente
        al mensaje.
        */

        setTimeout(
            () => {

                message.scrollIntoView(
                    {

                        behavior:
                            "smooth",

                        block:
                            "nearest"

                    }
                );

            },
            150
        );

    }

}



/* ==================================
   PEQUEÑO EFECTO DEL BOTÓN
================================== */

const messageButton =
    document.getElementById(
        "messageButton"
    );


messageButton.addEventListener(
    "click",
    function() {


        this.animate(

            [

                {
                    transform:
                        "scale(1)"
                },

                {
                    transform:
                        "scale(.94)"
                },

                {
                    transform:
                        "scale(1.04)"
                },

                {
                    transform:
                        "scale(1)"
                }

            ],

            {

                duration:
                    400,

                easing:
                    "ease-out"

            }

        );

    }
);


</script>


</body>

</html>
"""


@app.route("/")
def home():

    return render_template_string(
        HTML
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
