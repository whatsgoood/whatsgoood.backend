using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace WhatsGoodApi.Models.DBSettings
{
    public interface IPlagiarismDbSettings
    {
        string MacCollectionName { get; set; }
        string WindGuruCollectionName { get; set; }
        string MSWCollectionName { get; set; }
        string ConnectionString { get; set; }
        string DatabaseName { get; set; }
        
    }
}
