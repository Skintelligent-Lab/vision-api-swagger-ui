# vision-api-swagger-ui

API documentation for Skintelligent's vision API. The webpage is available at https://skintelligent-lab.github.io/vision-api-swagger-ui/

The API documentation is contained in `static/spec`; these files are automatically built and pushed to this repo during builds of the [vision API](https://github.com/Skintelligent-Lab/vision-api). The boilerplate HTML/JS is copied from [this repo](https://github.com/peter-evans/swagger-github-pages). The root document for the OpenAPI specification (currently `static/spec/openapi.yaml`) is controlled by the `url` argument to the `SwaggerUIBundle` constructor in the file `static/swagger-initializer.js`.


## Debugging & Development

To display API docs locally for development/debugging:

* `conda create -n swagger python=3.8 -y && conda activate swagger`
* `pip install -r requirements.txt`
* `export FLASK_APP=app.py`
* `export FLASK_DEBUG=true`
* `flask run --host 0.0.0.0 --port 5000`
