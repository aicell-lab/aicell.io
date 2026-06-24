# X (Twitter) watch-list for the lab newsletter

The nightly digest & the 3-hourly breaking-news scan sweep these via
`scripts/lab-x.py monitor`. All handles **verified live** against the API.
This is a **living list** — `scripts/lab-x.py discover` proposes new accounts that
many of our seeds follow; review and add the relevant ones (AI / agents / automation
/ cell biology / bioimaging / omics / virtual cell). Keep curated to the lab's vision;
prune noise.

## AI labs & orgs
@AnthropicAI · @OpenAI · @GoogleDeepMind · @AIatMeta · @huggingface · @MistralAI ·
@NVIDIAAI · @allen_ai · @deepseek_ai · @minimax_ai · @arcinstitute · @ChanZuckerberg · @biohub

## AI leaders & influencers
@karpathy · @ylecun · @sama · @JeffDean · @demishassabis · @drfeifei · @AndrewYNg ·
@hardmaru · @ilyasut · @gdb · @thom_wolf · @yoshua_bengio · @mmbronstein · @nathanbenaich

## AI for biology / computational biology
@MoAlQuraishi · @james_y_zou · @jure · @marinkazitnik · @fabian_theis · @anshulkundaje ·
@DaphneKoller · @BoWang87 · @stephenquake · @KrishnaswamyLab · @alexrives · @pdhsu ·
@ai4pathology · @elhamazizi · @euanashley

## Bioimaging, microscopy & cell biology
@florianjug · @loicaroyer · @HenriquesLab · @Prof_Lundberg · @rita_strack

## Medical / clinical AI
@EricTopol · @pranavrajpurkar · @jnkath

## Agent tooling & dev
@bcherny · @antigravity

## AI papers & news aggregators (high signal for trending work)
@_akhaliq · @iScienceLuvr · @omarsar0 · @rohanpaul_ai

## Journals, science news & venues
@natmachintell · @naturebiotech · @quantamagazine · @iclr_conf

---
### Living watch-list — keep growing it
- Each digest / scan: run `scripts/lab-x.py discover` and ask *"is there anyone new
  worth following?"* Verify a candidate with `scripts/lab-x.py info <handle>` (real
  person + followers + relevant bio), then add them above.
- Topic sweeps beyond accounts: `scripts/lab-x.py search "virtual cell AI" --max 20`.
- Note: Emma Lundberg = **@Prof_Lundberg** (the bare @emmalundberg is a different/inactive account).
  Anna Kreshuk, Aviv Regev, Charlotte Bunne have no verified active handle yet — add if found.
