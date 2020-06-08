# eventbridge-integration-solution-buildkite-visualization
## Amazon EventBridge Integration Solution for Buildkite Visualization

This Quick Start demonstrates an integration with AWS Lambda, Amazon S3, AWS Glue, and Amazon Athena for Amazon EventBridge SaaS Partner Buildkite. This solution enables your Amazon EventBridge event bus to trigger an EventBridge Rule that evaluates Builkite's "Job Finished" events. If events satisfy the Rule pattern, they are sent to Lambda, which extracts key metrics and puts them into S3. Additionally, Glue resources -- a Crawler, a JSON Classifier, and a Database -- are created and ready to crawl the S3 bucket *on demand* once events appear. Lastly, an example Athena Query is created, ready to query your Glue Database Table and act as a data source for Amazon QuickSight or a visualization tool of your choosing. 

![Quick Start architecture for EventBridge Integration Solution for Buildkite Visualization](https://github.com/aws-quickstart/eventbridge-integration-solution-buildkite-visualization/raw/master/images/arch-eventbridge-buildkite-visualization.png)


To post feedback, submit feature ideas, or report bugs, use the **Issues** section of [this GitHub repo](https://github.com/aws-quickstart/eventbridge-integration-solution-buildkite-visualization).