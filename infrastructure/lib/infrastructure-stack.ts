import * as cdk from "@aws-cdk/core";
import * as s3 from "@aws-cdk/aws-s3";
import * as eb from "@aws-cdk/aws-elasticbeanstalk";

export class InfrastructureStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const bucket = new s3.Bucket(this, `${id}-sources-bucket`, {});

    const app = new eb.CfnApplication(this, "Application", {
      applicationName: "dotnet-core-app",
    });

    const elbZipArchive = new s3assets.Asset(this, "MyElbAppZip", {
      path: `fix`,
    });

    const appVersionProps = new eb.CfnApplicationVersion(this, "AppVersion", {
      applicationName: "Tatoeba Sync",
      sourceBundle: {
        s3Bucket: elbZipArchive.s3BucketName,
        s3Key: elbZipArchive.s3ObjectKey,
      },
    });

    const elbEnv = new eb.CfnEnvironment(this, "Environment", {
      environmentName: "dotnet-core-env",
      applicationName: app.applicationName ?? "DotnetAppEnvName",
      solutionStackName: "64bit Amazon Linux 2 v2.1.2 running .NET Core",
      versionLabel: appVersionProps.ref,
    });

    // The code that defines your stack goes here
  }
}
