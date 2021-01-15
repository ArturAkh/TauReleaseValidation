#!/usr/local/bin/python3
  
import ROOT as R
import numpy as np
import json
from styles import ModTDRStyle
R.gROOT.SetBatch()
R.gStyle.SetOptStat(0)
R.gStyle.SetLegendBorderSize(1)
ModTDRStyle()
from tauIDEffsAndROCs import ptbins, etabins

colors = [R.kBlack, R.kRed+1, R.kCyan+2, R.kOrange+1, R.kMagenta+2, R.kGreen +2, R.kBlue, R.kYellow+3]
colordict = {
    "DNN based, 2017" : R.kMagenta+2,
    "BDT based, new DM, Phase 2" : R.kCyan+2,
    "BDT based, new DM, 2017" : R.kRed+1,
    "Isolation sum based, Phase 2" : R.kBlack,
}

ptbincenters = {
    "genuine" : np.array([(ptbins["genuine"][index] + ptbins["genuine"][index+1])/2.0 for index in range(len(ptbins["genuine"][:-1]))] + [ptbins["genuine"][-1]*1.1]),
    "jet" : np.array([(ptbins["jet"][index] + ptbins["jet"][index+1])/2.0 for index in range(len(ptbins["jet"][:-1]))] + [ptbins["jet"][-1]*1.1]),
    "electron" : np.array([(ptbins["electron"][index] + ptbins["electron"][index+1])/2.0 for index in range(len(ptbins["electron"][:-1]))] + [ptbins["electron"][-1]*1.1]),
    "muon" : np.array([(ptbins["muon"][index] + ptbins["muon"][index+1])/2.0 for index in range(len(ptbins["muon"][:-1]))] + [ptbins["muon"][-1]*1.1]),
}

etabincenters = {
    "genuine" : np.array([(etabins["genuine"][index] + etabins["genuine"][index+1])/2.0 for index in range(len(etabins["genuine"][:-1]))]),
    "jet" : np.array([(etabins["jet"][index] + etabins["jet"][index+1])/2.0 for index in range(len(etabins["jet"][:-1]))]),
    "electron" : np.array([(etabins["electron"][index] + etabins["electron"][index+1])/2.0 for index in range(len(etabins["electron"][:-1]))]),
    "muon" : np.array([(etabins["muon"][index] + etabins["muon"][index+1])/2.0 for index in range(len(etabins["muon"][:-1]))]),
}

ptbinwidths = {
    "genuine"   : np.array([(ptbins["genuine"][index] - ptbins["genuine"][index+1])/-2.0 for index in range(len(ptbins["genuine"][:-1]))] + [(ptbins["genuine"][-2] - ptbins["genuine"][-1])/-2.0]),
    "jet"       : np.array([(ptbins["jet"][index] - ptbins["jet"][index+1])/-2.0 for index in range(len(ptbins["jet"][:-1]))] + [(ptbins["jet"][-2] - ptbins["jet"][-1])/-2.0]),
    "electron" : np.array([(ptbins["electron"][index] - ptbins["electron"][index+1])/-2.0 for index in range(len(ptbins["electron"][:-1]))] + [(ptbins["electron"][-2] - ptbins["electron"][-1])/-2.0]),
    "muon"     : np.array([(ptbins["muon"][index] - ptbins["muon"][index+1])/-2.0 for index in range(len(ptbins["muon"][:-1]))] + [(ptbins["muon"][-2] - ptbins["muon"][-1])/-2.0]),
}

etabinwidths = {
    "genuine" : np.array([(etabins["genuine"][index] - etabins["genuine"][index+1])/-2.0 for index in range(len(etabins["genuine"][:-1]))]),
    "jet" : np.array([(etabins["jet"][index] - etabins["jet"][index+1])/-2.0 for index in range(len(etabins["jet"][:-1]))]),
    "electron" : np.array([(etabins["electron"][index] - etabins["electron"][index+1])/-2.0 for index in range(len(etabins["electron"][:-1]))]),
    "muon" : np.array([(etabins["muon"][index] - etabins["muon"][index+1])/-2.0 for index in range(len(etabins["muon"][:-1]))]),
}

barrel = False

if barrel:
    efficiencies = json.load(open("pt_efficiencies.json", "r"))
    eta_efficiencies = json.load(open("eta_efficiencies.json", "r"))
else:
    efficiencies = json.load(open("pt_efficiencies_endcap.json", "r"))
    eta_efficiencies = json.load(open("eta_efficiencies_endcap.json", "r"))


fake_minimum = {
    "against_jet" : 0.00005,
    "against_electron" : 0.00001,
    "against_muon" : 0.00001,
}

genuine_minimum = {
    "against_jet" : 0.0,
    "against_electron" : 0.0,
    "against_muon" : 0.0,
}

pt_fake_labels = {
    "against_jet" : "reconstructed p_{T}(jet)",
    "against_electron" : "generator p_{T}(e)",
    "against_muon" : "generator p_{T}(#mu)",
}

eta_fake_labels = {
    "against_jet" : "reconstructed #eta(jet)",
    "against_electron" : "generator #eta(e)",
    "against_muon" : "generator #eta(#mu)",
}

c = R.TCanvas()
c.cd()
c.SetLogy()

roc = {}
roc_3wps = {}
ptbinlabels = [
    "p_{T}(^{}#tau_{h}) #in [20, 40) GeV",
    "p_{T}(^{}#tau_{h}) #in [40, 60) GeV",
    "p_{T}(^{}#tau_{h}) #in [60, 80) GeV",
    "p_{T}(^{}#tau_{h}) #in [80, 100) GeV",
    "p_{T}(^{}#tau_{h}) #in [100, 120) GeV",
    "p_{T}(^{}#tau_{h}) #in [120, 160) GeV",
    "p_{T}(^{}#tau_{h}) #in [140, 200) GeV",
    "p_{T}(^{}#tau_{h}) #geq 200 GeV",
]

for disci, disc in enumerate(efficiencies["against_jet"]):
    roc[disc] = []
    roc_3wps[disc] = []

etalabel = "|#eta(^{}#tau_{h})| < 1.4" if barrel else "1.4 #leq |#eta(^{}#tau_{h})| < 3.0"

for ptbin in range(len(ptbinlabels)):
    legend = R.TLegend(0.2, 0.57, 0.5, 0.82) if barrel  and ptbin > 0 else R.TLegend(0.45, 0.12, 0.75, 0.37)
    legend.SetTextSize(0.035)
    legend.SetFillStyle(0)

    text = R.TLatex()
    text.SetNDC()
    text.SetTextAngle(0)
    text.SetTextColor(R.kBlack)
    text.SetTextAlign(11)
    text.SetTextFont(42)
    text.SetTextSize(0.045)
    for disci, disc in enumerate(efficiencies["against_jet"]):
        effs = efficiencies["against_jet"][disc]
        signal_effs_pt_bin1 = np.array([effs[WP]["genuine"][ptbin] for WP in reversed(effs.keys())])
        background_effs_pt_bin1 = np.array([effs[WP]["jet"][ptbin] for WP in reversed(effs.keys())])
        signal_effs_3wps = np.array([effs[WP]["genuine"][ptbin] for WP in reversed(effs.keys()) if not "VT" in WP and not "VL" in WP])
        background_effs_3wps = np.array([effs[WP]["jet"][ptbin] for WP in reversed(effs.keys()) if not "VT" in WP and not "VL" in WP])
        roc[disc].append(R.TGraph(len(signal_effs_pt_bin1), signal_effs_pt_bin1, background_effs_pt_bin1))
        roc[disc][ptbin].SetLineColor(colordict[disc])
        roc[disc][ptbin].SetLineWidth(3)
        roc[disc][ptbin].SetMarkerColor(colordict[disc])
        roc[disc][ptbin].SetMarkerSize(1.0)
        roc[disc][ptbin].SetMarkerStyle(8)
        roc_3wps[disc].append(R.TGraph(len(signal_effs_3wps), signal_effs_3wps, background_effs_3wps))
        roc_3wps[disc][ptbin].SetLineColor(colordict[disc])
        roc_3wps[disc][ptbin].SetLineWidth(3)
        roc_3wps[disc][ptbin].SetMarkerColor(colordict[disc])
        roc_3wps[disc][ptbin].SetMarkerSize(2.0)
        roc_3wps[disc][ptbin].SetMarkerStyle(4)
        legend.AddEntry(roc[disc][ptbin], disc, "lp")
        if disci == 0:
            roc[disc][ptbin].GetXaxis().SetLimits(0.0, 1.0)
            roc[disc][ptbin].GetXaxis().SetTitle("genuine ^{}#tau_{h} efficiency")
            roc[disc][ptbin].GetYaxis().SetRangeUser(0.0001, 1.0)
            roc[disc][ptbin].GetYaxis().SetTitle("Jet #rightarrow ^{}#tau_{h} efficiency")
            roc[disc][ptbin].Draw("apl")
            roc_3wps[disc][ptbin].Draw("p same")
        else:
            roc[disc][ptbin].Draw("pl same")
            roc_3wps[disc][ptbin].Draw("p same")
    legend.Draw()
    text.DrawLatex(0.2, 0.87, ", ".join([ptbinlabels[ptbin], etalabel]))

    c.SaveAs("roc_ptbin%s_%s.png"%(str(ptbin), "barrel" if barrel else "endcap"))
    c.Print("roc_ptbin%s_%s.pdf"%(str(ptbin), "barrel" if barrel else "endcap"))
