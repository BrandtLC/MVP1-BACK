from flask import Flask
from flask_cors import CORS
import mysql.connector
from flask_swagger_ui import get_swaggerui_blueprint


class Server():

    def __init__(self, ):
        SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
        API_URL = 'http://petstore.swagger.io/v2/swagger.json'  # Our API url (can of course be a local resource)

        self.app = Flask(__name__)
        self.app.json.sort_keys = False
        CORS(self.app, resources={r"/*": {"origins": "*"}})

        self.db = mysql.connector.connect(
          host='localhost',
          user='root',
          password='Br@va1372',
          database='mvp1'
        )

        swaggerui_blueprint = get_swaggerui_blueprint(
            SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
            API_URL,
            config={  # Swagger UI config overrides
                'app_name': "Test application"
            },
            #  oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
            #     'clientId': "your-client-id",
            #     'clientSecret': "your-client-secret-if-required",
            #     'realm': "your-realms",
            #     'appName': "your-app-name",
            #     'scopeSeparator': " ",
            #     'additionalQueryStringParams': {'test': "hello"}
            #  }
        )
        self.app.register_blueprint(swaggerui_blueprint)

    def run(self, ):
        self.app.run(
          debug=True,

        )


server = Server()
