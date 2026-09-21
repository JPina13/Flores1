from flask import Flask, render_template_string

app = Flask(__name__)

HTML = r"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Unas flores para ti 💛</title>
    <style>
        * { box-sizing: border-box; }

        body {
            margin: 0;
            min-height: 100vh;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: "Segoe UI", sans-serif;
            background: linear-gradient(135deg, #fff8c9, #ffe680, #fff3ad);
            color: #5b4300;
        }

        .card {
            width: min(92%, 430px);
            padding: 35px 22px;
            text-align: center;
            border-radius: 28px;
            background: rgba(255, 255, 255, 0.55);
            box-shadow: 0 12px 40px rgba(130, 94, 0, 0.18);
            backdrop-filter: blur(8px);
            z-index: 2;
        }

        h1 {
            margin: 0 0 12px;
            font-size: clamp(2rem, 8vw, 3rem);
            color: #c58a00;
        }

        p {
            font-size: 1.1rem;
            line-height: 1.6;
            margin: 10px 0;
        }

        .bouquet {
            position: relative;
            height: 280px;
            margin: 10px auto 20px;
        }

        .flower {
            position: absolute;
            left: 50%;
            bottom: 40px;
            width: 95px;
            height: 95px;
            transform: translateX(-50%);
            animation: sway 3s ease-in-out infinite;
        }

        .flower:nth-child(1) { margin-left: -95px; bottom: 75px; transform: scale(.82); }
        .flower:nth-child(2) { margin-left: 85px; bottom: 70px; transform: scale(.85); animation-delay: .5s; }
        .flower:nth-child(3) { margin-left: 0; bottom: 125px; transform: scale(1.05); animation-delay: 1s; }
        .flower:nth-child(4) { margin-left: -45px; bottom: 25px; transform: scale(.7); animation-delay: 1.5s; }
        .flower:nth-child(5) { margin-left: 45px; bottom: 25px; transform: scale(.72); animation-delay: 2s; }

        .petals {
            position: absolute;
            inset: 0;
            border-radius: 50%;
            background:
                radial-gradient(ellipse at 50% 10%, #ffd21f 0 22%, transparent 23%),
                radial-gradient(ellipse at 90% 30%, #ffd21f 0 22%, transparent 23%),
                radial-gradient(ellipse at 82% 78%, #ffd21f 0 22%, transparent 23%),
                radial-gradient(ellipse at 18% 78%, #ffd21f 0 22%, transparent 23%),
                radial-gradient(ellipse at 10% 30%, #ffd21f 0 22%, transparent 23%);
            transform: rotate(18deg);
        }

        .center {
            position: absolute;
            width: 38%;
            height: 38%;
            top: 31%;
            left: 31%;
            border-radius: 50%;
            background: radial-gradient(circle, #6b4300, #3e2800);
            box-shadow: 0 0 0 5px rgba(255, 188, 0, .35);
        }

        .stem {
            position: absolute;
            left: 50%;
            top: 75px;
            width: 8px;
            height: 190px;
            background: #4d8a35;
            border-radius: 10px;
            transform: rotate(-8deg);
            transform-origin: top;
            z-index: -1;
        }

        .leaf {
            position: absolute;
            width: 75px;
            height: 32px;
            background: #5b9c3b;
            border-radius: 100% 0 100% 0;
            top: 170px;
            left: 42%;
            transform: rotate(-28deg);
        }

        .leaf.right {
            left: 51%;
            transform: rotate(28deg) scaleX(-1);
        }

        .ribbon {
            display: inline-block;
            margin-top: 10px;
            padding: 10px 22px;
            border-radius: 30px;
            background: #e5ae16;
            color: white;
            font-weight: bold;
            cursor: pointer;
            border: none;
            font-size: 1rem;
        }

        #message {
            display: none;
            margin-top: 18px;
            font-style: italic;
            animation: appear .8s ease;
        }

        .petal {
            position: absolute;
            top: -30px;
            width: 14px;
            height: 20px;
            background: #ffd21f;
            border-radius: 100% 0 100% 0;
            animation: fall linear infinite;
            opacity: .8;
        }

        @keyframes sway {
            0%, 100% { rotate: -3deg; }
            50% { rotate: 3deg; }
        }

        @keyframes fall {
            to {
                transform: translateY(110vh) rotate(720deg);
            }
        }

        @keyframes appear {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body>
    <div id="petals"></div>

    <main class="card">
        <h1>Estas flores son para ti 💛</h1>
        <p>Porque hay personas que hacen la vida un poquito más bonita.</p>

        <div class="bouquet">
            <div class="stem"></div>
            <div class="leaf"></div>
            <div class="leaf right"></div>

            <div class="flower"><div class="petals"></div><div class="center"></div></div>
            <div class="flower"><div class="petals"></div><div class="center"></div></div>
            <div class="flower"><div class="petals"></div><div class="center"></div></div>
            <div class="flower"><div class="petals"></div><div class="center"></div></div>
            <div class="flower"><div class="petals"></div><div class="center"></div></div>
        </div>

        <p>Hechas con mucho cariño 🌻</p>
        <button class="ribbon" onclick="showMessage()">Tengo algo que decirte</button>
        <p id="message">Gracias por existir y por hacer mis días más bonitos. 💛</p>
    </main>

    <script>
        const container = document.getElementById("petals");

        for (let i = 0; i < 24; i++) {
            const petal = document.createElement("div");
            petal.className = "petal";
            petal.style.left = Math.random() * 100 + "vw";
            petal.style.animationDuration = (5 + Math.random() * 7) + "s";
            petal.style.animationDelay = (-Math.random() * 10) + "s";
            petal.style.transform = `rotate(${Math.random() * 360}deg)`;
            container.appendChild(petal);
        }

        function showMessage() {
            document.getElementById("message").style.display = "block";
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
