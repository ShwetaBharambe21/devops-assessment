from flask import Flask
import redis

app = Flask(__name__)

r = redis.Redis(host='redis-service', port=6379)

@app.route("/")
def hello():
    r.incr('hits')
    count = r.get('hits').decode()
    return f"Hello DevOps! Total Hits: {count}"

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)