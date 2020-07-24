from mlflow import log_metric, log_param, log_artifact

if __name__ == "__main__":
    # Log a parameter (key-value pair)
    log_param("param1", 10)

    # Log a metric; metrics can be updated throughout the run
    log_metric("foo", 50)
    log_metric("foo", 130)
    log_metric("foo", 200)

    # Log an artifact (output file)
    with open("output.txt", "w") as f:
        f.write("Hello world!")
    log_artifact("output.txt")
