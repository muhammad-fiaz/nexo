import os
from flask import Flask, render_template

app = Flask(__name__)

def get_template_routes():
    template_folder = 'templates'
    routes = []

    for filename in os.listdir(template_folder):
        if filename.endswith('.html'):
            route = filename.split('.')[0]
            routes.append(route)

    return routes

template_routes = get_template_routes()

for route in template_routes:
    @app.route(f'/{route}')
    def dynamic_route():
        return render_template(f'{route}.html')

if __name__ == '__main__':
    app.run(debug=True)



