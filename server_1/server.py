from flask import Flask,request,jsonify, send_file,render_template
import util
import matplotlib.pyplot as plt
import pandas as pd
import io
import base64
import csv
import matplotlib
matplotlib.use('Agg')

from flask_cors import CORS
app=Flask(__name__)
CORS(app)

# @app.route('/')
# def index():
#     # Generate the graph
#     with open('./artifacts/flipkart3 - flipkart3.csv', 'r', encoding='utf-8') as file:
#         reader = csv.reader(file)
#         df8 = pd.DataFrame(reader)
#         category_counts = df8[2].value_counts().head(10)
#         categories = category_counts.index.tolist()
#         counts = category_counts.tolist()
#
#         # Adjust the figure size
#         plt.figure(figsize=(12, 8))  # Adjust the width and height as needed
#         plt.gca().set_facecolor('darkgrey')  # Set the background color
#
#         # Plot the graph
#         bar_colors = 'white'  # Color for the bars
#         label_colors = 'black'  # Color for the labels
#
#         # Plot the graph
#         plt.barh(categories, counts,color=bar_colors)  # Use barh for horizontal bar chart
#         plt.xlabel('Number of Products', color=label_colors)
#         plt.ylabel('Product Category', color=label_colors)
#         plt.title('Top 10 Product Categories', color=label_colors)
#         plt.xticks(fontsize=10, color=label_colors)  # Adjust font size for x-axis labels
#
#         # Save the graph to a file
#         graph_path = './artifacts/graph.png'
#         plt.tight_layout()  # Adjust the spacing between subplots
#         plt.savefig(graph_path, format='png')
#         plt.close()
#         print("graph loaded")
#
#     return send_file(graph_path, mimetype='image/png')
#
# @app.route('/')
# def index1():
#     # Generate the graph
#     with open('./artifacts/flipkart3 - flipkart3.csv', 'r', encoding='utf-8') as file:
#         reader = csv.reader(file)
#         df8 = pd.DataFrame(reader)
#         brand_counts = df8[6].value_counts().head(10)
#         brands = brand_counts.index.tolist()
#         counts = brand_counts.tolist()
#
#         # Adjust the figure size
#         plt.figure(figsize=(12, 8))  # Adjust the width and height as needed
#         plt.gca().set_facecolor('darkgrey')  # Set the background color
#
#         # Plot the graph
#         bar_colors = 'white'  # Color for the bars
#         label_colors = 'black'  # Color for the labels
#
#         # Plot the graph
#         plt.bar(brands, counts,color=bar_colors)  # Use barh for horizontal bar chart
#         plt.xlabel('Brand', color=label_colors)
#         plt.ylabel('Name of the product', color=label_colors)
#         plt.title('Top 10 Product brands', color=label_colors)
#         plt.xticks(fontsize=10, color=label_colors)  # Adjust font size for x-axis labels
#
#         # Save the graph to a file
#         graph_path = './artifacts/graph1.png'
#         plt.tight_layout()  # Adjust the spacing between subplots
#         plt.savefig(graph_path, format='png')
#         plt.close()
#         print("graph1 loaded")
#
#     return send_file(graph_path, mimetype='image/png')



@app.route('/')
def index():
    # Generate the first graph
    with open('./artifacts/flipkart3 - flipkart3.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        df8 = pd.DataFrame(reader)
        category_counts = df8[2].value_counts().head(10)
        categories = category_counts.index.tolist()
        counts = category_counts.tolist()
        # plt.style.use('dark_background')

        # Adjust the figure size

        fig = plt.figure(figsize=(15, 10))
        fig.patch.set_facecolor('#82674900')
        ax = fig.add_subplot(111)
        # plt.figure(figsize=(15, 10))
        ax = plt.gca()
        ax.set_facecolor('#82674900')

        # Plot the first graph
        bar_colors = 'black'
        label_colors = 'black'
        plt.barh(categories, counts, color=bar_colors)
        plt.xlabel('Number of Products', color=label_colors,fontsize=18)
        plt.ylabel('Product Category', color=label_colors,fontsize=18)
        # plt.title('Top 10 Product Categories', color=label_colors)
        plt.xticks(fontsize=14, color=label_colors)
        plt.yticks(fontsize=10)

        # Save the first graph to a file
        graph1_path = './artifacts/graph1.png'
        plt.tight_layout()
        plt.savefig(graph1_path, format='png')
        plt.close()
        print("graph1 loaded")

    # Generate the second graph
    with open('./artifacts/flipkart3 - flipkart3.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        df8 = pd.DataFrame(reader)
        brand_counts = df8[6].value_counts().head(10)
        brands = brand_counts.index.tolist()
        counts = brand_counts.tolist()

        # Adjust the figure size
        # plt.figure(figsize=(15, 10))
        fig = plt.figure(figsize=(15, 10))
        fig.patch.set_facecolor('#82674900')
        ax = fig.add_subplot(111)
        ax = plt.gca()
        ax.set_facecolor('#82674900')


        # Plot the second graph
        bar_colors = 'black'
        label_colors = 'black'
        plt.bar(brands, counts, color=bar_colors)
        plt.xlabel('Brand', color=label_colors,fontsize=18)
        plt.ylabel('Name of the product', color=label_colors,fontsize=18)
        # plt.title('Top 10 Product Brands', color=label_colors)
        plt.xticks(fontsize=12, color=label_colors)
        plt.yticks(fontsize=14)

        # Save the second graph to a file
        graph2_path = './artifacts/graph2.png'
        plt.tight_layout()
        plt.savefig(graph2_path, format='png')
        plt.close()
        print("graph2 loaded")

    return send_file(graph1_path, mimetype='image/png'), send_file(graph2_path, mimetype='image/png')


@app.route('/get_category_names')
def get_category_names():
    response = jsonify({
        'categories': util.get_category_names()
    })
    # print(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_brands')
def get_brands():
    category = request.args.get('category')
    response = jsonify({
        'brands': util.get_brands(category)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_products')
def get_products():
    category = request.args.get('category')
    brand = request.args.get('brand')
    response = jsonify({
        'product': util.get_products(category,brand)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_price')
def predict_price():
    try:
        product=request.args.get('product')
        category = request.args.get('category')
        brand = request.args.get('brand')
        discount = int(request.args.get('discount'))
        print(discount)
        param1, param2, param3 = util.predict_price(product, brand, category, discount)

        response = jsonify({
            'predict_price': param1,
            'discount': param2,
            'retail': param3
        })

        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__=="__main__":
    print("starting server")
    print(util.predict_price("3a AUTOCARE Car Mat Chevrolet Beat",'3a AUTOCARE','''["Automotive >> Accessories & Spare parts >> Car Interior & Exterior >> Car Interior >> Car Mats"]''',1490))
    app.run()

