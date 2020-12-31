using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using System.Text.Json;

namespace backend.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class JibikiProxyController : ControllerBase
    {
        private ILogger<JibikiProxyController> Logger { get; }
        private HttpClient Client { get; }

        public JibikiProxyController(ILogger<JibikiProxyController> logger, HttpClient httpClient)
        {
            Logger = logger;
            Client = httpClient;
        }

        [HttpGet("{query}")]
        public async Task<IEnumerable<JibikiSentenceResponse>> Get(string query)
        {
            var response = await Client.GetAsync($"https://api.jibiki.app/sentences?query={query}");
            return JsonSerializer.Deserialize<List<JibikiSentenceResponse>>(response.Content.ReadAsStringAsync().Result);
        }
    }
}
