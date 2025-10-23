from flask import Flask, render_template_string

app = Flask(__name__)

# HTML template embedded in Python
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>National Park</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
        }

        .credit-tag {
            color: white;
            font-size: 1rem;
            margin-top: 1rem;
            opacity: 0.9;
            font-style: italic;
        }

        .hero {
            background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), 
                        url('https://images.unsplash.com/photo-1564760055775-d63b17a55c44?w=1600') center/cover;
            height: 95vh;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            color: white;
        }

        .hero-content h1 {
            font-size: 4rem;
            margin-bottom: 1rem;
            text-shadow: 3px 3px 6px rgba(0,0,0,0.7);
        }

        .hero-content p {
            font-size: 1.5rem;
            margin-bottom: 2rem;
        }

        .btn {
            display: inline-block;
            padding: 1rem 2rem;
            background: #FF9933;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            transition: all 0.3s;
            font-weight: bold;
        }

        .btn:hover {
            background: #e68a2e;
            transform: scale(1.05);
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 4rem 2rem;
        }

        .section-title {
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 3rem;
            color: #138808;
        }

        .parks-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-bottom: 4rem;
        }

        .park-card {
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.3s;
            border-top: 4px solid #FF9933;
        }

        .park-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 8px 12px rgba(0,0,0,0.2);
        }

        .park-card img {
            width: 100%;
            height: 200px;
            object-fit: cover;
            background: #e0e0e0;
        }

        .park-info {
            padding: 1.5rem;
        }

        .park-info h3 {
            color: #138808;
            margin-bottom: 0.5rem;
            font-size: 1.5rem;
        }

        .park-info .location {
            color: #FF9933;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }

        .features {
            background: #f9f9f9;
            padding: 4rem 2rem;
        }

        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }

        .feature-item {
            background: white;
            padding: 2rem;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .icon {
            font-size: 3rem;
            margin-bottom: 1rem;
        }

        .feature-item h3 {
            color: #138808;
            margin-bottom: 1rem;
        }

        .about-author {
            background: linear-gradient(135deg, #FF9933 0%, #138808 100%);
            color: white;
            padding: 4rem 2rem;
        }

        .about-content {
            max-width: 800px;
            margin: 0 auto;
            text-align: center;
        }

        .author-name {
            font-size: 3rem;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        .author-title {
            font-size: 1.3rem;
            margin-bottom: 2rem;
            opacity: 0.95;
        }

        .author-bio {
            font-size: 1.1rem;
            line-height: 1.8;
            background: rgba(255,255,255,0.1);
            padding: 2rem;
            border-radius: 10px;
            backdrop-filter: blur(10px);
        }

        .skills {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 1rem;
            margin-top: 2rem;
        }

        .skill-tag {
            background: rgba(255,255,255,0.2);
            padding: 0.5rem 1.5rem;
            border-radius: 20px;
            font-weight: 600;
        }

        footer {
            background: #000080;
            color: white;
            text-align: center;
            padding: 2rem;
        }

        .footer-content {
            max-width: 800px;
            margin: 0 auto;
        }
    </style>
</head>
<body>
    <section class="hero">
        <div class="hero-content">
            <h1>🇮🇳 India's National Parks</h1>
            <p>Exploring India's Incredible Wildlife Heritage</p>
            <a href="#parks" class="btn">Discover the Wild</a>
            <p class="credit-tag">- By Shreyash</p>
        </div>
    </section>

    <section id="parks" style="background: white; padding: 4rem 2rem;">
        <div class="container">
            <h2 class="section-title">Featured National Parks</h2>
            <div class="parks-grid">
                <div class="park-card">
                    <img src="https://images.unsplash.com/photo-1564760055775-d63b17a55c44?w=600" alt="Tiger">
                    <div class="park-info">
                        <h3>Jim Corbett National Park</h3>
                        <p class="location">📍 Uttarakhand</p>
                        <p>India's oldest national park, established in 1936. Famous for Bengal tigers and rich biodiversity in the Himalayan foothills.</p>
                    </div>
                </div>

                <div class="park-card">
                    <img src="https://www.insideindianjungles.com/wp-content/uploads/2019/07/kaziranga.jpg" alt="Rhinoceros" onerror="this.src='https://source.unsplash.com/600x400/?rhinoceros,wildlife'">
                    <div class="park-info">
                        <h3>Kaziranga National Park</h3>
                        <p class="location">📍 Assam</p>
                        <p>UNESCO World Heritage Site, home to two-thirds of the world's one-horned rhinoceros population. A true conservation success story.</p>
                    </div>
                </div>

                <div class="park-card">
                    <img src="https://www.india-tours.com/wildlife/images/wildlife/national-parks/sasan-gir-national-park.jpg" alt="Lion" onerror="this.src='https://source.unsplash.com/600x400/?lion,wildlife'">
                    <div class="park-info">
                        <h3>Gir National Park</h3>
                        <p class="location">📍 Gujarat</p>
                        <p>The last refuge of the Asiatic lion. This park is the only place in the world where you can spot wild Asiatic lions in their natural habitat.</p>
                    </div>
                </div>

                <div class="park-card">
                    <img src="https://images.unsplash.com/photo-1549366021-9f761d450615?w=600" alt="Birds">
                    <div class="park-info">
                        <h3>Ranthambore National Park</h3>
                        <p class="location">📍 Rajasthan</p>
                        <p>Famous for its tiger population and historic ruins. One of the best places in India to spot tigers during daytime safaris.</p>
                    </div>
                </div>

                <div class="park-card">
                    <img src="https://images.unsplash.com/photo-1589182373726-e4f658ab50f0?w=600" alt="Mountains">
                    <div class="park-info">
                        <h3>Bandipur National Park</h3>
                        <p class="location">📍 Karnataka</p>
                        <p>Part of the Nilgiri Biosphere Reserve. Known for large elephant herds and being one of the premier tiger reserves in South India.</p>
                    </div>
                </div>

                <div class="park-card">
                    <img src="https://images.unsplash.com/photo-1614027164847-1b28cfe1df60?w=600" alt="Wildlife">
                    <div class="park-info">
                        <h3>Periyar National Park</h3>
                        <p class="location">📍 Kerala</p>
                        <p>A beautiful wildlife sanctuary centered around Periyar Lake. Famous for elephants, tigers, and boat safaris through scenic landscapes.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="features">
        <h2 class="section-title">Why National Parks Matter</h2>
        <div class="feature-grid">
            <div class="feature-item">
                <div class="icon">🐅</div>
                <h3>Wildlife Conservation</h3>
                <p>Protecting endangered species like tigers, rhinos, and lions from extinction</p>
            </div>
            <div class="feature-item">
                <div class="icon">🌳</div>
                <h3>Ecosystem Preservation</h3>
                <p>Maintaining biodiversity and protecting natural habitats for future generations</p>
            </div>
            <div class="feature-item">
                <div class="icon">🔬</div>
                <h3>Research & Education</h3>
                <p>Providing opportunities for scientific research and environmental education</p>
            </div>
            <div class="feature-item">
                <div class="icon">💚</div>
                <h3>Sustainable Tourism</h3>
                <p>Promoting eco-tourism while supporting local communities and conservation efforts</p>
            </div>
        </div>
    </section>

    <section class="about-author">
        <div class="about-content">
            <h2 class="author-name">About Shreyash</h2>
            <div class="author-bio">
                <p>Hello! I'm Shreyash, a passionate programmer. 
                This project is my initiative to raise awareness about India's magnificent national parks and the importance of wildlife conservation.</p>
                <br>
                <p>Through this website, I aim to showcase the beauty and diversity of India's protected areas, inspire more people to visit these natural wonders, 
                and highlight the critical role these parks play in preserving our biodiversity. I believe that nature conservation can work hand in hand 
                to create a better future for our planet.</p>
            </div>
        </div>
    </section>

    <footer>
        <div class="footer-content">
            <p style="font-size: 1.2rem; margin-bottom: 1rem;">🇮🇳 India's National Parks</p>
            <p>&copy; 2025 - A Project by Shreyash</p>
            <p style="margin-top: 1rem; opacity: 0.9;">Created with passion for wildlife conservation and web development</p>
        </div>
    </footer>
</body>
</html>
'''


@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


