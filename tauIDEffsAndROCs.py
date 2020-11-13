#!/usr/local/bin/python3
  
import ROOT as R
import numpy as np
import json
R.gROOT.SetBatch()
R.gStyle.SetOptStat(0)
R.gStyle.SetLegendBorderSize(0)

def construct_binning(binning_structure):
    bins = np.concatenate([np.arange(start, end, step) for start, end, step in binning_structure] + [np.array([binning_structure[-1][1]])])
    return bins

do_preprocessing = False
do_disc = True and do_preprocessing
do_wps = False and do_preprocessing
do_rocs = False and do_preprocessing
do_pt_binned = True and do_preprocessing
do_eta_binned = True and do_preprocessing

ptbins  = {
#    "genuine" : construct_binning([[20.0, 100.0, 10.0], [100.0, 500.0, 50.0]]),
    "genuine" : construct_binning([[20.0, 120.0, 20.0], [120.0, 200.0, 40.0]]),
    #"jet" : construct_binning([[20.0, 100.0, 10.0], [100.0, 150.0, 50.0]]),
    "jet" : construct_binning([[20.0, 120.0, 20.0], [120.0, 200.0, 40.0]]),
    "electron" : construct_binning([[20.0, 70.0, 10.0]]),
    "muon" : construct_binning([[20.0, 60.0, 10.0]]),
}

#etabins  = {
#    "genuine"  : construct_binning([[-3.2, 3.2, 0.2]]),
#    "jet"      : construct_binning([[-3.2, 3.2, 0.2]]),
#    "electron" : construct_binning([[-3.2, 3.2, 0.2]]),
#    "muon"     : construct_binning([[-3.2, 3.2, 0.2]]),
#}

etabins  = {
    "genuine"  : construct_binning([[-1.4, 1.4, 0.2]]),
    "jet"      : construct_binning([[-1.4, 1.4, 0.2]]),
    "electron" : construct_binning([[-1.4, 1.4, 0.2]]),
    "muon"     : construct_binning([[-1.4, 1.4, 0.2]]),
}
### Definitions:
# DeepTau vs jet: all 8
# DeepTau vs electron: all 8
# DeepTau vs muon: all 4 
# BDT vs jet: no VVVLoose, so 7
# BDT vs electron: 5
wps = ["VVVLoose", "VVLoose", "VLoose", "Loose", "Medium", "Tight", "VTight", "VVTight"]
colors = [R.kBlack, R.kRed+1, R.kCyan+2, R.kOrange+1, R.kMagenta+2, R.kGreen +2, R.kBlue, R.kYellow+3]

names = {
    "genuine" : R.std.vector('string')(),
    "jet" : R.std.vector('string')(),
}

fake_minimum = {
    "against_jet" : 0.0004,
    "against_electron" : 0.0004,
    "against_muon" : 0.0001,
}

genuine_minimum = {
    "against_jet" : 0.3,
    "against_electron" : 0.3,
    "against_muon" : 0.75,
}

[names["genuine"].push_back("%s_val.root"%p) for p in ["ZTT","ZpTT", "TenTaus"]]
#[names["genuine"].push_back("%s_val.root"%p) for p in ["ZTT"]]
[names["jet"].push_back("%s_val.root"%p)for p in ["TTbar", "QCD"]]
#[names["jet"].push_back("%s_val.root"%p)for p in ["QCD"]]

#baseline = "(tau_dm < 5 || tau_dm > 7) && tau_decayModeFindingNewDMs > 0.5 && tau_pt > 20.0 && tau_genpt > 20.0"
#baseline = "(tau_genpt > 20.0 && abs(tau_geneta) < 3.0)"
baseline = "(tau_genpt > 20.0 && abs(tau_geneta) < 1.4)"
#nominator_cuts  = "(tau_decayModeFinding > 0.5 && tau_pt > 20.0 && abs(tau_eta) < 3.0)"
#nominator_cuts  = "(tau_decayModeFinding > 0.5 && tau_pt > 20.0 && abs(tau_eta) < 1.4)"
nominator_cuts  = "(tau_decayModeFindingNewDMs > 0.5 && (tau_dm < 5 || tau_dm > 7) && tau_pt > 20.0 && abs(tau_eta) < 1.4)"


combined_iso_phase2 = "(tau_chargedIsoPtSum + 0.2 * TMath::Max(0.0, tau_neutralIsoPtSumdR03 - ((abs(tau_eta) < 1.4)*5.0 + (abs(tau_eta) >= 1.4)*1.0)))"

discriminators = {
    "against_jet" : {
        "DNN based, 2017"                  :            {"key" : "deep_tau", "expression" : "tau_byDeepTau2017v2p1VSjetraw"},
        "BDT based, new DM, Phase 2"       : {"key" : "bdt_phase2", "expression" : "0.5*(tau_byIsolationMVADBnewDMwLTPhase2raw + 1.0)"},
        "BDT based, new DM, 2017"          :    {"key" : "bdt_newDM",  "expression" : "0.5*(tau_byIsolationMVArun2017v2DBnewDMwLTraw2017 + 1.0)"},
#        "BDT based, old DM, 2017"          :    {"key" : "bdt_oldDM",  "expression" : "0.5*(tau_byIsolationMVArun2017v2DBoldDMwLTraw2017 + 1.0)"},
#        "Isolation sum based"              :    {"key" : "combined_iso",  "expression" : "-1.0*tau_byCombinedIsolationDeltaBetaCorrRaw3Hits*(tau_byCombinedIsolationDeltaBetaCorrRaw3Hits < 101.0) - 101.0*(tau_byCombinedIsolationDeltaBetaCorrRaw3Hits >= 101.0)"},
        "Isolation sum based, Phase 2"     :    {"key" : "combined_iso_phase2",  "expression" : "-1.0*{COMBISO}*({COMBISO} < 101.0) - 101.0*({COMBISO} >= 101.0)".format(COMBISO=combined_iso_phase2)},
    },
    "against_electron" : {
        "DNN based, 2017" :            {"key" : "deep_tau", "expression" : "tau_byDeepTau2017v2p1VSeraw"},
        "BDT based, Phase 2" : {"key" : "bdt_phase2", "expression" : "0.5*(tau_againstElectronMVA6RawPhase2v1 + 1.0)"},
        "BDT based, 2018" :    {"key" : "bdt_2018",  "expression" : "0.5*(tau_againstElectronMVA6Raw2018 + 1.0)"},
        "BDT based, 2016" :    {"key" : "bdt_2016",  "expression" : "0.5*(tau_againstElectronMVA6Raw + 1.0)"},
    },
    "against_muon" : {
        "DNN based, 2017" :            {"key" : "deep_tau", "expression" : "tau_byDeepTau2017v2p1VSmuraw"},
    },
}

discriminator_wps = {
    "against_jet" : {
        "DNN based, 2017" :            {"key" : "deep_tau", "wps" : ["tau_by{WP}DeepTau2017v2p1VSjet".format(WP=wp) for wp in wps]},
        "BDT based, new DM, Phase 2" : {"key" : "bdt_phase2", "wps" : ["tau_by{WP}IsolationMVADBnewDMwLTPhase2".format(WP=wp) for wp in wps[1:]]},
        "BDT based, new DM, 2017" :    {"key" : "bdt_newDM", "wps" : ["tau_by{WP}IsolationMVArun2017v2DBnewDMwLT2017 ".format(WP=wp) for wp in wps[1:]]},
#        "BDT based, old DM, 2017" :    {"key" : "bdt_oldDM", "wps" : ["tau_by{WP}IsolationMVArun2017v2DBoldDMwLT2017".format(WP=wp) for wp in wps[1:]]},
#        "Isolation sum based"     :    {"key" : "combined_iso", "wps" : ["tau_by{WP}CombinedIsolationDeltaBetaCorr3Hits".format(WP=wp) for wp in wps[3:6]]},
        "Isolation sum based, Phase 2"     :    {"key" : "combined_iso_phase2", "wps" : ["tau_by{WP}CombinedIsolationPhase2".format(WP=wp) for wp in wps[3:7]]},
    },
    "against_electron" : {
        "DNN based, 2017" :            {"key" : "deep_tau", "wps" : ["tau_by{WP}DeepTau2017v2p1VSe".format(WP=wp) for wp in wps]},
        "BDT based, Phase 2" : {"key" : "bdt_phase2", "wps" : ["tau_againstElectron{WP}MVA6Phase2v1".format(WP=wp) for wp in wps[2:7]]},
        "BDT based, 2018" :    {"key" : "bdt_2018", "wps" : ["tau_againstElectron{WP}MVA62018".format(WP=wp) for wp in wps[2:7]]},
        "BDT based, 2016" :    {"key" : "bdt_2016", "wps" : ["tau_againstElectron{WP}MVA6".format(WP=wp) for wp in wps[2:7]]},
    },
    "against_muon" : {
        "DNN based, 2017" :            {"key" : "deep_tau", "wps" : ["tau_by{WP}DeepTau2017v2p1VSmu".format(WP=wp) for wp in wps[2:6]]},
        "Cut based" :            {"key" : "cut_based", "wps" : ["tau_againstMuon{WP}3".format(WP=wp) for wp in ["Loose", "Tight"]]},
    },
}

results = {}
wp_results = {}

c = R.TCanvas()
c.cd()

if do_preprocessing:
    taus = {
        "genuine" : R.RDataFrame("per_tau",names["genuine"]).Filter(baseline),
        "jet" : R.RDataFrame("per_tau",names["jet"]).Filter(baseline),
        "muon" : R.RDataFrame("per_tau","ZMM_val.root").Filter(baseline),
        "electron" : R.RDataFrame("per_tau","ZEE_val.root").Filter(baseline),
    }

    n_true = taus["genuine"].Count().GetValue()
    n_jet = taus["jet"].Count().GetValue()
    n_e = taus["electron"].Count().GetValue()
    n_mu = taus["muon"].Count().GetValue()

    print("n_true =",n_true)
    print("n_jet =",n_jet)
    print("n_e =",n_e)
    print("n_mu =",n_mu)


    ptbinselections = {
        "genuine" : [],
        "jet" : [],
        "muon" : [],
        "electron" : [],
    }

    for dtype in ptbinselections:
        for ptlow, pthigh in zip(ptbins[dtype][:-1], ptbins[dtype][1:]):
            ptbinselections[dtype].append(taus[dtype].Filter("tau_genpt >= {LOW} && tau_genpt < {HIGH}".format(LOW=ptlow,HIGH=pthigh)))
        ptbinselections[dtype].append(taus[dtype].Filter("tau_genpt >= {HIGH}".format(HIGH=ptbins[dtype][-1])))

    ptbinnevents = {
        "genuine" : [ptbin.Count().GetValue() for ptbin in ptbinselections["genuine"]],
        "jet" : [ptbin.Count().GetValue() for ptbin in ptbinselections["jet"]],
        "muon" : [ptbin.Count().GetValue() for ptbin in ptbinselections["muon"]],
        "electron" : [ptbin.Count().GetValue() for ptbin in ptbinselections["electron"]],
    }

    etabinselections = {
        "genuine" : [],
        "jet" : [],
        "muon" : [],
        "electron" : [],
    }

    for dtype in etabinselections:
        for etalow, etahigh in zip(etabins[dtype][:-1], etabins[dtype][1:]):
            etabinselections[dtype].append(taus[dtype].Filter("tau_geneta >= {LOW} && tau_geneta < {HIGH}".format(LOW=etalow,HIGH=etahigh)))


    etabinnevents = {
        "genuine" : [etabin.Count().GetValue() for etabin in etabinselections["genuine"]],
        "jet" : [etabin.Count().GetValue() for etabin in etabinselections["jet"]],
        "muon" : [etabin.Count().GetValue() for etabin in etabinselections["muon"]],
        "electron" : [etabin.Count().GetValue() for etabin in etabinselections["electron"]],
    }

if do_disc:
    for dtype in discriminators:
        results[dtype] = {}
        wp_results[dtype] = {}
        for name, exp in discriminators[dtype].items():
            fake = dtype.replace("against_","")
            histargs = ("","",102,-0.01,1.01) if "sum based" not in name else ("", "", 102, -101.0, 1.0)
            results[dtype][name] = {
                "genuine" : taus["genuine"].Define(exp["key"], exp["expression"]).Histo1D(histargs, exp["key"]),
                 fake     : taus[fake].Define(exp["key"], exp["expression"]).Histo1D(histargs, exp["key"]),
            }
            results[dtype][name]["genuine"].Scale(1.0/taus["genuine"].Count().GetValue())
            results[dtype][name]["genuine"].SetLineColor(R.kCyan+2)
            results[dtype][name]["genuine"].SetLineWidth(3)
            results[dtype][name]["genuine"].GetXaxis().SetTitle(name)
            results[dtype][name]["genuine"].GetXaxis().SetTitleSize(0.05)
            results[dtype][name]["genuine"].GetXaxis().SetTitleOffset(0.8)
            results[dtype][name][fake].Scale(1.0/taus[fake].Count().GetValue())
            results[dtype][name][fake].SetLineColor(R.kOrange+1)
            results[dtype][name][fake].SetLineWidth(3)
            results[dtype][name]["genuine"].SetMaximum(1.2*max(results[dtype][name]["genuine"].GetMaximum(), results[dtype][name][fake].GetMaximum()))

            results[dtype][name]["genuine"].Draw("hist")
            results[dtype][name][fake].Draw("histsame")

            legend = R.TLegend(0.4, 0.6, 0.7, 0.75)
            legend.SetTextSize(0.06)
            legend.AddEntry(results[dtype][name]["genuine"].GetValue(), "genuine tau", "L")
            legend.AddEntry(results[dtype][name][fake].GetValue(),      "%s to tau"%fake, "L")
            legend.Draw()

            c.Print("%s_%s.pdf"%(dtype,exp["key"]))
            c.SaveAs("%s_%s.png"%(dtype,exp["key"]))
            c.Clear()
if do_wps:
    for dtype in discriminator_wps:
        wp_results[dtype] = {}
        for name, exp in discriminator_wps[dtype].items():
            fake = dtype.replace("against_","")
            wp_results[dtype][name] = { "genuine" : [], fake : [] }
            for wp in discriminator_wps[dtype][name]["wps"]:
                if discriminator_wps[dtype][name]["key"] == "combined_iso_phase2":
                    cut = ""
                    if "VTight" in wp:
                        cut = "%s < 1.2 && %s"%(combined_iso_phase2,nominator_cuts)
                    elif "Tight" in wp:
                        cut = "%s < 2.0 && %s"%(combined_iso_phase2,nominator_cuts)
                    elif "Medium" in wp:
                        cut = "%s < 4.0 && %s"%(combined_iso_phase2,nominator_cuts)
                    elif "Loose" in wp:
                        cut = "%s < 5.0 && %s"%(combined_iso_phase2,nominator_cuts)
                    else:
                        print("No WP found!")
                        exit(0)
                    wp_results[dtype][name]["genuine"].append(taus["genuine"].Filter(cut).Count().GetValue()/taus["genuine"].Count().GetValue())
                    wp_results[dtype][name][fake].append(taus[fake].Filter(cut).Count().GetValue()/taus[fake].Count().GetValue())
                else:
                    wp_results[dtype][name]["genuine"].append(taus["genuine"].Filter("%s > 0.5 && %s"%(wp,nominator_cuts)).Count().GetValue()/taus["genuine"].Count().GetValue())
                    wp_results[dtype][name][fake].append(taus[fake].Filter("%s > 0.5 && %s"%(wp,nominator_cuts)).Count().GetValue()/taus[fake].Count().GetValue())

if do_rocs and do_wps and do_disc:
    rocs = {}

    for dtype in discriminators:
        rocs[dtype] = {}
        index = 0
        legend = R.TLegend(0.52, 0.15, 0.82, 0.4)
        legend.SetTextSize(0.035)
        legend.SetFillStyle(0)
        for name, exp in discriminators[dtype].items():
            rocs[dtype][name] = {}
            fake = dtype.replace("against_","")
            rocs[dtype][name][fake+"_eff"] = results[dtype][name][fake].GetCumulative(False)
            rocs[dtype][name]["genuine_eff"] = results[dtype][name]["genuine"].GetCumulative(False)
            g_effs = np.array([1.0] + [rocs[dtype][name]["genuine_eff"].GetBinContent(i+1) for i in range(rocs[dtype][name]["genuine_eff"].GetNbinsX())] + [0.0])
            f_effs = np.array([1.0] + [rocs[dtype][name][fake+"_eff"].GetBinContent(i+1) for i in range(rocs[dtype][name][fake+"_eff"].GetNbinsX())]     + [0.0])
            rocs[dtype][name]["roc"] = R.TGraph(len(g_effs), f_effs, g_effs)
            rocs[dtype][name]["roc"].SetLineColor(colors[index])
            rocs[dtype][name]["roc"].SetLineWidth(3)
            rocs[dtype][name]["roc"].SetMarkerColor(colors[index])
            rocs[dtype][name]["roc"].SetMarkerSize(1.0)
            rocs[dtype][name]["roc"].SetMarkerStyle(8)
            
            legend.AddEntry(rocs[dtype][name]["roc"], name, "lp")
            if index == 0:
                rocs[dtype][name]["genuine_eff"].SetMaximum(1.0)
                rocs[dtype][name]["genuine_eff"].SetMinimum(genuine_minimum[dtype])
                rocs[dtype][name]["genuine_eff"].GetXaxis().SetLimits(fake_minimum[dtype],1.0)
                rocs[dtype][name]["genuine_eff"].GetYaxis().SetTitle("genuine tau efficiency")
                rocs[dtype][name]["genuine_eff"].GetYaxis().SetTitleOffset(1.0)
                rocs[dtype][name]["genuine_eff"].GetYaxis().SetTitleSize(0.05)
                rocs[dtype][name]["genuine_eff"].GetXaxis().SetTitle("%s to tau efficiency"%fake)
                rocs[dtype][name]["genuine_eff"].GetXaxis().SetTitleSize(0.05)
                rocs[dtype][name]["genuine_eff"].Draw("axis")
            rocs[dtype][name]["roc"].Draw("l same")

            if discriminator_wps[dtype].get(name):
                rocs[dtype][name]["roc_wps"] = R.TGraph(len(discriminator_wps[dtype][name]["wps"]), np.array(wp_results[dtype][name][fake]), np.array(wp_results[dtype][name]["genuine"]))
                rocs[dtype][name]["roc_wps"].SetMarkerColor(colors[index])
                rocs[dtype][name]["roc_wps"].SetMarkerSize(1.0)
                rocs[dtype][name]["roc_wps"].SetMarkerStyle(8)
                rocs[dtype][name]["roc_wps"].Draw("p same")

            index += 1

        if dtype == "against_muon":
            name = "Cut based"
            rocs[dtype][name] = {}
            rocs[dtype][name]["roc_wps"] = R.TGraph(len(discriminator_wps[dtype][name]["wps"]), np.array(wp_results[dtype][name][fake]), np.array(wp_results[dtype][name]["genuine"]))
            rocs[dtype][name]["roc_wps"].SetMarkerColor(colors[index])
            rocs[dtype][name]["roc_wps"].SetMarkerSize(1.0)
            rocs[dtype][name]["roc_wps"].SetMarkerStyle(8)
            rocs[dtype][name]["roc_wps"].Draw("p same")
            legend.AddEntry(rocs[dtype][name]["roc_wps"], name, "p")
        c.SetLogx()
        legend.Draw()
        c.Print("%s_roc.pdf"%dtype)
        c.SaveAs("%s_roc.png"%dtype)
        c.Clear()

if do_pt_binned:
    wp_results_ptbinned = {}
    for dtype in discriminator_wps:
        print("type:",dtype)
        wp_results_ptbinned[dtype] = {}
        for name, exp in discriminator_wps[dtype].items():
            print("\tdiscriminator:",exp["key"])
            fake = dtype.replace("against_","")
            wp_results_ptbinned[dtype][name] = {}
            for wp in discriminator_wps[dtype][name]["wps"]:
                print("\t\twp:",wp)
                wp_results_ptbinned[dtype][name][wp] = { "genuine" : [], fake : [], "genuine_nevents" : [], fake+"_nevents" : [] }
                for index, genuineptbin in enumerate(ptbinselections["genuine"]):
                    genuinetotal = ptbinnevents["genuine"][index]
                    wp_results_ptbinned[dtype][name][wp]["genuine_nevents"].append(genuinetotal)
                    if genuinetotal > 0.0:
                        if discriminator_wps[dtype][name]["key"] == "combined_iso_phase2":
                            cut = ""
                            if "VTight" in wp:
                                cut = "%s < 1.2 && %s"%(combined_iso_phase2,nominator_cuts)
                            elif "Tight" in wp:
                                cut = "%s < 2.0 && %s"%(combined_iso_phase2,nominator_cuts)
                            elif "Medium" in wp:
                                cut = "%s < 4.0 && %s"%(combined_iso_phase2,nominator_cuts)
                            elif "Loose" in wp:
                                cut = "%s < 5.0 && %s"%(combined_iso_phase2,nominator_cuts)
                            else:
                                print("No WP found!")
                                exit(0)
                            wp_results_ptbinned[dtype][name][wp]["genuine"].append(genuineptbin.Filter(cut).Count().GetValue()/genuinetotal)
                        else:
                            wp_results_ptbinned[dtype][name][wp]["genuine"].append(genuineptbin.Filter("%s > 0.5 && %s"%(wp,nominator_cuts)).Count().GetValue()/genuinetotal)
                    else:
                        wp_results_ptbinned[dtype][name][wp]["genuine"].append(0.0)
                for index, fakeptbin in enumerate(ptbinselections[fake]):
                    faketotal = ptbinnevents[fake][index]
                    wp_results_ptbinned[dtype][name][wp][fake+"_nevents"].append(faketotal)
                    if faketotal > 0.0:
                        if discriminator_wps[dtype][name]["key"] == "combined_iso_phase2":
                            cut = ""
                            if "VTight" in wp:
                                cut = "%s < 1.2 && %s"%(combined_iso_phase2,nominator_cuts)
                            elif "Tight" in wp:
                                cut = "%s < 2.0 && %s"%(combined_iso_phase2,nominator_cuts)
                            elif "Medium" in wp:
                                cut = "%s < 4.0 && %s"%(combined_iso_phase2,nominator_cuts)
                            elif "Loose" in wp:
                                cut = "%s < 5.0 && %s"%(combined_iso_phase2,nominator_cuts)
                            else:
                                print("No WP found!")
                                exit(0)
                            wp_results_ptbinned[dtype][name][wp][fake].append(fakeptbin.Filter(cut).Count().GetValue()/faketotal)
                        else:
                            wp_results_ptbinned[dtype][name][wp][fake].append(fakeptbin.Filter("%s > 0.5 && %s"%(wp,nominator_cuts)).Count().GetValue()/faketotal)
                    else:
                        wp_results_ptbinned[dtype][name][wp][fake].append(0.0)
                
                print("\t\tgenuine:",wp_results_ptbinned[dtype][name][wp]["genuine"])
                print("\t\tfake:",wp_results_ptbinned[dtype][name][wp][fake])
                print("\t\tgenuine (evt):",wp_results_ptbinned[dtype][name][wp]["genuine_nevents"])
                print("\t\tfake (evt):",wp_results_ptbinned[dtype][name][wp][fake+"_nevents"])

    with open("pt_efficiencies.json", "w") as f:
        json.dump(wp_results_ptbinned, f, indent=2)

if do_eta_binned:
    wp_results_etabinned = {}
    for dtype in discriminator_wps:
        print("type:",dtype)
        wp_results_etabinned[dtype] = {}
        for name, exp in discriminator_wps[dtype].items():
            print("\tdiscriminator:",exp["key"])
            fake = dtype.replace("against_","")
            wp_results_etabinned[dtype][name] = {}
            for wp in discriminator_wps[dtype][name]["wps"]:
                print("\t\twp:",wp)
                wp_results_etabinned[dtype][name][wp] = { "genuine" : [], fake : [], "genuine_nevents" : [], fake+"_nevents" : [] }
                for index, genuineetabin in enumerate(etabinselections["genuine"]):
                    genuinetotal = etabinnevents["genuine"][index]
                    wp_results_etabinned[dtype][name][wp]["genuine_nevents"].append(genuinetotal)
                    if genuinetotal > 0.0:
                        if discriminator_wps[dtype][name]["key"] == "combined_iso_phase2":
                            cut = ""
                            if "VTight" in wp:
                                cut = "%s < 1.2 && %s"%(combined_iso_phase2,nominator_cuts)
                            elif "Tight" in wp:
                                cut = "%s < 2.0 && %s"%(combined_iso_phase2,nominator_cuts)
                            elif "Medium" in wp:
                                cut = "%s < 4.0 && %s"%(combined_iso_phase2,nominator_cuts)
                            elif "Loose" in wp:
                                cut = "%s < 5.0 && %s"%(combined_iso_phase2,nominator_cuts)
                            else:
                                print("No WP found!")
                                exit(0)
                            wp_results_etabinned[dtype][name][wp]["genuine"].append(genuineetabin.Filter(cut).Count().GetValue()/genuinetotal)
                        else:
                            wp_results_etabinned[dtype][name][wp]["genuine"].append(genuineetabin.Filter("%s > 0.5 && %s"%(wp,nominator_cuts)).Count().GetValue()/genuinetotal)
                    else:
                        wp_results_etabinned[dtype][name][wp]["genuine"].append(0.0)
                for index, fakeetabin in enumerate(etabinselections[fake]):
                    faketotal = etabinnevents[fake][index]
                    wp_results_etabinned[dtype][name][wp][fake+"_nevents"].append(faketotal)
                    if faketotal > 0.0:
                        if discriminator_wps[dtype][name]["key"] == "combined_iso_phase2":
                            cut = ""
                            if "VTight" in wp:
                                cut = "%s < 1.2 && %s"%(combined_iso_phase2,nominator_cuts)
                            elif "Tight" in wp:
                                cut = "%s < 2.0 && %s"%(combined_iso_phase2,nominator_cuts)
                            elif "Medium" in wp:
                                cut = "%s < 4.0 && %s"%(combined_iso_phase2,nominator_cuts)
                            elif "Loose" in wp:
                                cut = "%s < 5.0 && %s"%(combined_iso_phase2,nominator_cuts)
                            else:
                                print("No WP found!")
                                exit(0)
                            wp_results_etabinned[dtype][name][wp][fake].append(fakeetabin.Filter(cut).Count().GetValue()/faketotal)
                        else:
                            wp_results_etabinned[dtype][name][wp][fake].append(fakeetabin.Filter("%s > 0.5 && %s"%(wp,nominator_cuts)).Count().GetValue()/faketotal)
                    else:
                        wp_results_etabinned[dtype][name][wp][fake].append(0.0)
                
                print("\t\tgenuine:",wp_results_etabinned[dtype][name][wp]["genuine"])
                print("\t\tfake:",wp_results_etabinned[dtype][name][wp][fake])
                print("\t\tgenuine (evt):",wp_results_etabinned[dtype][name][wp]["genuine_nevents"])
                print("\t\tfake (evt):",wp_results_etabinned[dtype][name][wp][fake+"_nevents"])
    with open("eta_efficiencies.json", "w") as f:
        json.dump(wp_results_etabinned, f, indent=2)
