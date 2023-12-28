from covabra import Covabra
from core.utils import difference, log_this_guy

cic_covabra = Covabra()
cic_covabra.banco_connection("CIC")
cic_covabra.banco_engine()
cic_covabra.banco_session()

erp_covabra = Covabra()
erp_covabra.banco_connection("ERP")
erp_covabra.banco_engine()

venda_covabra = Covabra()
venda_covabra.banco_connection("VENDA")
venda_covabra.banco_engine()
pdvs_df = venda_covabra.banco_query("core/sql/find_pdvs_venda.sql") # DataFrame PDVs
pdvs = pdvs_df.apply(lambda row: f"192.168.{row['nestab']}.{100+row['npdv']}", axis=1) # Series PDVs IPs
# ERP Promotions'
df1_erp = erp_covabra.banco_query("core/sql/find_promo_header_erp.sql")
df2_erp = erp_covabra.banco_query("core/sql/find_promo_content_erp.sql")

df2_erp_all = erp_covabra.banco_query("core/sql/find_promo_content_all_erp.sql")

# PDV Promotions
for pdv in pdvs:
    # PDV MySQL Connection
    pdv_covabra = Covabra()
    try:
        pdv_covabra.banco_connection("OUTRO", driver="mysql+mysqlconnector", host=f"{pdv}", database="PDV", port="3306", user="root", password="")
        pdv_covabra.banco_engine()

        df1_pdv = pdv_covabra.banco_query("core/sql/find_promo_header_pdv.sql")
        df2_pdv = pdv_covabra.banco_query("core/sql/find_promo_content_pdv.sql")
        
        diff1 = difference(df1_pdv, df1_erp)
        diff2 = difference(df2_pdv, df2_erp)

        if not diff1.empty:
            diff1.to_sql("promocaopersonalizada", con=pdv_covabra.banco_engine(), if_exists="append", index=False)

            log_result = log_this_guy(pdv=pdv, msg="DIVERGÊNCIA EM HEADER")
            log_result.to_sql("log_promocionapdvs", con=cic_covabra.banco_engine(), if_exists="append", index=False)

        if not diff2.empty:
            divergencia = df2_erp_all.loc[df2_erp_all['idproduto'].isin(diff2['idproduto'])] #  Preservar a descrição da Promoção procurando em um DataFrame completo.
            divergencia.to_sql("promocaopersonalizadaproduto", con=pdv_covabra.banco_engine(), if_exists="append", index=False)

            log_result = log_this_guy(pdv=pdv, msg="DIVERGÊNCIA EM CONTENT")
            log_result.to_sql("log_promocionapdvs", con=cic_covabra.banco_engine(), if_exists="append", index=False)

    except:
        log_result = log_this_guy(pdv=pdv, msg="INOPERANTE")
        log_result.to_sql("log_promocionapdvs", con=cic_covabra.banco_engine(), if_exists="append", index=False)