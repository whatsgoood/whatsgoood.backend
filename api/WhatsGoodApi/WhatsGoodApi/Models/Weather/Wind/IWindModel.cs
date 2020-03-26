using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace WhatsGoodApi.Models.Weather.Wind
{
    public interface IWindModel
    {
        string Id { get; set; }
        decimal avg { get; set; }
        decimal low { get; set; }
        decimal high { get; set; }
        string direction { get; set; }
    }
}
