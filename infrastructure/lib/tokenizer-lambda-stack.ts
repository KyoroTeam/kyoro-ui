import * as cdk from "@aws-cdk/core";
import * as ec2 from "@aws-cdk/aws-ec2";
import * as s3 from "@aws-cdk/aws-s3";
import * as efs from "@aws-cdk/aws-efs";
import * as lambda from "@aws-cdk/aws-lambda";
import * as path from 'path';

// The tokenizer lambdas will use Kuromoji to tokenize sentences.
// It is ran when the user uploads custom source text into a bucket
// afterwards needs to update Meilisearch with the new indicies.

export class TokenizerLambdaStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    var kuromojiIpadicLambda = new lambda.Function(this, "ipadic-tokenizer-lambda", {
        runtime: lambda.Runtime.JAVA_11,
        handler: "hander.index",
        code: lambda.Code.fromAsset(path.join(__dirname, 'lambda-handler')),
    })
  }
}