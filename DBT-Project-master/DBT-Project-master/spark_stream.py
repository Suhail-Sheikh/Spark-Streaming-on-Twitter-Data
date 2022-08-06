from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import functions as F
from pyspark.streaming import StreamingContext
from pyspark.sql.context import SQLContext


def preprocessing(lines):
    words = lines.select(explode(split(lines.value, "t_end")).alias("word"))
    words = words.na.replace('', None)
    words = words.na.drop()
    words = words.withColumn('word', F.regexp_replace('word', r'http\S+', ''))
    words = words.withColumn('word', F.regexp_replace('word', '@\w+', ''))
    words = words.withColumn('word', F.regexp_replace('word', '#', ''))
    words = words.withColumn('word', F.regexp_replace('word', 'RT', ''))
    words = words.withColumn('word', F.regexp_replace('word', ':', ''))
    return words


if __name__ == "__main__":
    # create Spark session
    spark = SparkSession.builder.appName(
        "TwitterSentimentAnalysis").getOrCreate()
    ssc = StreamingContext(spark, 5)
    sqlContext = SQLContext(spark)
    lines = ssc.socketTextStream("127.0.0.1", 8081)
    # lines = spark.readStream.format("socket").option(
    #     "host", "127.0.0.1").option("port", 8081).load()
    # Preprocess the data
    words = preprocessing(lines)
    print(words)
    # query = words.writeStream.queryName("all_tweets")\
    #     .outputMode("append").format("parquet")\
    #     .option("path", "./parc")\
    #     .option("checkpointLocation", "./check")\
    #     .trigger(processingTime='60 seconds').start()
    # query.awaitTermination()
