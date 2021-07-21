import { Application, Router } from "https://deno.land/x/oak@v8.0.0/mod.ts";
import { oakCors } from "https://deno.land/x/cors@v1.2.2/mod.ts";

const content = Deno.readTextFileSync("./all_v11_out.json");
const SentenceData = JSON.parse(content) as any[];

const router = new Router();

console.log("Ready to Run");

router
  .get("/getLocalContentList", (context) => {
    console.log("getLocalContentList");
    const sources = SentenceData.map((d) => d.Source);
    const uniqueSources = new Set(sources);
    context.response.body = Array.from(uniqueSources.values());
  })
  .get("/getTokenizedSentences/:sourceId", (context) => {
    const source = context.params.sourceId;
    console.log("getTokenizedSentences", source);
    const sources = SentenceData.filter((d) => d.Source === source);
    context.response.body = sources;
  });

const app = new Application();
app.use(oakCors());
app.use(router.routes());
app.use(router.allowedMethods());

await app.listen({ port: 8006 });
