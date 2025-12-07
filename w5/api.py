from flask import Flask, jsonify, request
from .fib import fibonacci, fibonacci_sequence_cached


app = Flask(__name__)

@app.get("/fib")
def fib_endpoint():
    # lee parámetro n de la query, por ejemplo /fib?n=10
    n = int(request.args.get("n", 10))
    seq = fibonacci(n)
    return jsonify(sequence=seq)

@app.get("/fib-cached")
def fib_endpoint_cached():
    # lee parámetro n de la query, por ejemplo /fib?n=10
    n = int(request.args.get("n", 10))
    seq = fibonacci_sequence_cached(n)
    return jsonify(sequence=seq)

if __name__ == "__main__":
    # importante escuchar en 0.0.0.0 para que sea accesible dentro del contenedor
    app.run(host="0.0.0.0", port=8000)