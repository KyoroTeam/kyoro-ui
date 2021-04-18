import type { JibikiSenteceResponse } from "src/models/Jibiki";
import type { ISentenceSource } from "./searchService";

export default class JibikiSenteceSource implements ISentenceSource {
  name: string = "Jibiki";

  async searchSentences(keyword: string): Promise<JibikiSenteceResponse[]> {
    const searchQuery = encodeURIComponent(keyword);
    const url = `https://cors.bridged.cc/https://api.jibiki.app/sentences?query=${searchQuery}`;
    return new Promise((resolve) => {
      fetch(url)
        .then((r) => r.json())
        .then((value: JibikiSenteceResponse[]) => resolve(value))
        .catch(() => resolve([]));
    });
  }
}
