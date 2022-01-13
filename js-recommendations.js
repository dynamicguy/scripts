importClass(org.apache.solr.common.SolrInputDocument);
importClass(org.apache.solr.client.solrj.response.QueryResponse);
importClass(org.apache.solr.client.solrj.SolrQuery);
importClass(org.apache.solr.common.SolrDocumentList);
importClass(org.apache.solr.client.solrj.impl.NoOpResponseParser);


var orig_q = request.getFirstParam("q");

//try {

//var server = solrServerFactory.getSolrServer("ecomm1_signals_aggr");
var server = solrServerFactory.getSolrServer("products_signals_aggr");

var params = new SolrQuery();

params.setParam("q",orig_q);
params.setParam("mm","50%");
params.setParam("pf","query_t^3","query_t~2^7");
params.setParam("fl","id","doc_id_s","weight_d");
params.setParam("sort","score desc,weight_d desc");
params.setParam("qf","query_t");
params.setParam("fq","aggr_type_s:*")
params.setParam("rows","100");
params.setParam("defType","edismax");
params.setParam("wt","json");

for (var x=0;x<request.getParam("fq").size();x++) {

    var fq = request.getParam("fq").get(x);
    if (fq.startsWith("{!term f=brand_NAME_s}")) {
        var brand = fq.split("}")[1];

        brand = brand.replace(" ","_");
        brand = brand.toLowerCase();
        brand = brand.replace("&amp;","&");
        request.addParam("test",brand);
        params.setParam("fq","filters_orig_ss:brand/"+brand);
    }
}



//var response = server.query(params);
//var list = response.getResults();
var dontMessWithSolr = new NoOpResponseParser();
dontMessWithSolr.setWriterType("json");

//_context("subquery-results",response);
_context.setProperty("subquery-results",response);
//if brand is chosen, filter recommendations to this brand only.

//request.addParam("test",request.getParam("fq").get(0))



//build the bq
/*var bq = "";

 for (var i=0;i<list.size();i++) {
 var doc = list.get(i);
 bq += "id:"+doc.getFieldValue("doc_id_s")+"^"+doc.getFieldValue("weight_d") + " ";
 }

 request.addParam("bq",bq);*/

//} catch(e) {
//  logger.error("Error getting recommendations:");
//  logger.error(e);
//}

