# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 16:31:29 2020

@author: halil
"""


baglaclar=[",",";","ama","amma","ancak","açıkçası","adeta","âdeta","bari","belki","bile","bir başka deyişle","binaenaleyh",
           "dahi","de","demek","demek ki","dışında","eğer","fakat","gene","gelgelelim","gerek","gerekse","gâh","gibi","hatta",
           "halbuki","hâlbuki","hazır","hakeza","hele","hem","kaldı ki","karşın","kâh","keşke","keza","kısaca","ki","lakin",
           "lâkin","madem","mademki","mamafih","maydamı","meğerki","meğerse","nasıl ki","ne var ki","ne yazık ki","nitekim",
           "neyse","oysa","oysaki","öyle ki","öyleyse","üstelik","sanki","sonra","sonra da","ve","ve de","velakin","velev",
           "velhâsıl","velhâsılıkelâm","veya","veyahut","ya da","yahut","yalınız","yalnız","yani","yeter ki","yine","yok",
           "yoksa","zaten","zati","zira","çünkü","ile","illa","illa ki","ille velakin","ille velâkin","imdi","ise"]

kisaltList=["age.","agm.","agy.","Alb.","Alm.","anat.","ant.","Apt.","Ar.","ark.","Arş.","Gör.","As.","As.","İz.","Asb.","astr.",
        "astrol.","Atğm.","atm.","Av.","bağ.","Bçvş.","bit.","b.","biy.","bk.","bl.","Bl.","Bn.","Bnb.","bot.","Böl.","bs.",
        "Bşk.","Bul.","Bulg.","Cad.","coğ.","Cum.","Bşk.","çev.","Çvş.","db.","dil","b.","dk.","Doç.","doğ.","Dr.","drl.",
        "Dz.","Kuv.","Dz.","Kuv.","K.","dzl.","Ecz.","ed.","e.","ekon.","Ens.","Erm.","f.","Fak.","Far.","fel.","fil.","fiz.",
        "fizy.","Fr.","Gen.","geom.","gn.","Gnkur.","Gön.","gr.","hay.","b.","haz.","hek.","hlk.","Hs.","Uzm.","huk.","Hv.","Kuv.",
        "Hv.","Kuv.","K.","Hz.","öz.","Hz.","İbr.","İng.","is.","İsp.","işl.","İt.","Jap.","jeol.","kim.","koor.","Kor.",
        "Kora.","Korg.","kr.","krş.","Kur.","Kur.","Bşk.","Lat.","Ltd.","Mac.","Mah.","man.","mat.","Md.","mec.","mim.",
        "min.","Müh.","Mür.","müz.","No.","Nö.","Nö.","Sb.","Okt.","Onb.","Opr.","Or.","Ora.","Ord.","Org.","Ort.","Osm.","T.",
        "öl.","ör.","öz.","ped.","Port.","Prof.","psikol.","Rum.","Rus.","s.","sa.","Sb.","SEFD","Bşk.","sf.","Sl.","Sn.",
        "snt.","Sok.","sos.","sp.","Srp.","Şb.","T.","T.C.","tar.","Tb.","tek.","tel.","telg.","Tğm.","tic.","tiy.","tlks.",
        "tls.","Top.","Tug.","Tuğa.","Tuğg.","Tüm.","Tüma.","Tümg.","Uzm.","Üçvş.","ünl.","Ütğm.","vb.","vd.","Vet.","vs.",
        "Y.","Mim.","Y.","Müh.","Yay.","Yb.","Yd.","Sb.","Yrd.","Yrd.","Doç.","Yun.","yy.","Yzb.","zf.","zm.","zool.",
        "St.","Sh.","Yd.","İnş.","Tic.", "Bkz.","Tur.","İşl","San.","Yat.","İst."]