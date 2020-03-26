using MongoDB.Driver;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using WhatsGoodApi.Models.Weather.Wind;
using WhatsGoodApi.Models.DBSettings;

namespace WhatsGoodApi.Services
{
    public class WindWeatherService
    {

        private readonly IMongoCollection<WindModel> _macWindModels;
        private readonly IMongoCollection<WindModel> _windGuruModels;

        public WindWeatherService(IPlagiarismDbSettings settings)
        {
            var constr = Environment.GetEnvironmentVariable("WHATSGOOD_CONSTR");
            var client = new MongoClient(constr);
            var database = client.GetDatabase(settings.DatabaseName);

            _macWindModels = database.GetCollection<WindModel>(settings.MacCollectionName);
            _windGuruModels = database.GetCollection<WindModel>(settings.WindGuruCollectionName);

        }

        public WindModel GetLatest()
        {
            var macModelList = _macWindModels.Find(windModel => true).ToList();

            if (macModelList.Count() == 0)
                return null;

            return macModelList.Last();
            //implement averaging of wind data here.
        }



    }
}
