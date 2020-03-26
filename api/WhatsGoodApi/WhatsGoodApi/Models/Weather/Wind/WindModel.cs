using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace WhatsGoodApi.Models.Weather.Wind
{
    public class WindModel : IWindModel
    {
        [BsonId]
        [BsonRepresentation(BsonType.ObjectId)]
        public string Id { get; set; }
        public decimal avg { get; set; }
        public decimal low { get; set; }
        public decimal high { get; set; }
        public string direction { get; set; }

    }
}
