import * as cdk from "@aws-cdk/core";
import * as ec2 from "@aws-cdk/aws-ec2";
import * as s3 from "@aws-cdk/aws-s3";
import * as efs from "@aws-cdk/aws-efs";
import * as eb from "@aws-cdk/aws-elasticbeanstalk";

export class InfrastructureStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const vpc = new ec2.Vpc(this, `${id}-app-vpc`, {
      enableDnsSupport: true,
      enableDnsHostnames: true,
    });

    const bucket = new s3.Bucket(this, `${id}-sources-bucket`, {});

    const app = new eb.CfnApplication(this, "Application", {
      applicationName: "dotnet-core-app",
    });

    const elbZipArchive = new s3assets.Asset(this, "MyElbAppZip", {
      path: `fix`,
    });

    const appVersionProps = new eb.CfnApplicationVersion(this, "AppVersion", {
      applicationName: "MeiliSearch",
      sourceBundle: {
        s3Bucket: elbZipArchive.s3BucketName,
        s3Key: elbZipArchive.s3ObjectKey,
      },
    });

    const ebGroup = new ec2.SecurityGroup(this, "group", {
      vpc: vpc,
    });

    const elbEnv = new eb.CfnEnvironment(this, "Environment", {
      environmentName: `${id}-meilisearch-environment`,
      applicationName: "MeiliSearch",
      solutionStackName: "64bit Amazon Linux 2 v3.3.0 running Docker",
      versionLabel: appVersionProps.ref,
      optionSettings: [
        {
          namespace: "aws:ec2:vpc",
          optionName: "VPCId",
          value: vpc.vpcId,
        },
        {
          namespace: "aws:autoscaling:launchconfiguration",
          optionName: "SecurityGroups",
          value: ebGroup.securityGroupId,
        },
      ],
    });

    const filesystem = new efs.FileSystem(this, `${id}-meilisearch-fs`, {
      vpc: vpc,
      lifecyclePolicy: efs.LifecyclePolicy.AFTER_7_DAYS,
    });

    filesystem.connections.addSecurityGroup(ebGroup);

    // The code that defines your stack goes here
  }
}
