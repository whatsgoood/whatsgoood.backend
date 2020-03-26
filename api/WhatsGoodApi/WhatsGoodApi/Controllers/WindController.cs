using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using WhatsGoodApi.Models.Prediction;
using WhatsGoodApi.Models.Weather.Wind;
using WhatsGoodApi.Services;

namespace WhatsGoodApi.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class WindController : Controller
    {
        private readonly WindWeatherService _windWeatherService;
        public WindController (WindWeatherService windWeatherService)
        {
            _windWeatherService = windWeatherService;
        }

        // GET: Wind
        [HttpGet]
        public ActionResult<IWindModel> Get()
        {
            WindModel wm = _windWeatherService.GetLatest();

            if (wm == null) 
                return NotFound();

            return wm;
        }

        //public ActionResult<PredictionModel> Prediction()
        //{



        //}

        // GET: Wind/Details/5
        public ActionResult Details(int id)
        {
            return View();
        }

    }
}