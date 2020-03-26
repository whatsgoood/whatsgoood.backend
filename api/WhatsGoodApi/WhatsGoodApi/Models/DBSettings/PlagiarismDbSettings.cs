using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace WhatsGoodApi.Models.DBSettings
{
    public class PlagiarismDbSettings : IPlagiarismDbSettings
    {
        public string MacCollectionName { get; set; }
        public string WindGuruCollectionName { get; set; }
        public string MSWCollectionName { get; set; }
        public string ConnectionString { get; set; }
        public string DatabaseName { get; set; }
    }
}
