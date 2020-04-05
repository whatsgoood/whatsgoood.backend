from flask import Flask
app = Flask(__name__)

@app.route('/api/sport-rating-list')
def sportRatingList():
    # TODO: 
    #
    # 1) Connect to MongoDB
    #
    # 2) Build rating for each sport
    #    using sport-specific weights
    #
    # Example: 
    #     Kiting would have wind weighted high
    #     in comparision to the temperature

    return {
        "sportRating": [
            {
                "name": "kiting",
                "rating": 6.2 
            },
            {
                "name": "surfing",
                "rating": 9.4 
            },
            {
                "name": "climbing",
                "rating": 2.0 
            }
        ]
    }

if __name__ == '__main__':
    app.run()