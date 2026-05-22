# Data Storage Guide — UCL Biosciences
**Note**. This is a work-in-progress - some details may need updating/amending.

> **Who is this for?** PIs, postdocs, and PhD students who need to store, share, or archive research data at UCL.  
> A separate guide covers HPC-specific storage (Myriad scratch, Lustre, etc.).

---

## Quick decision guide

```mermaid
flowchart TD
    A([What kind of data?]) --> B{Research data?}

    B -- Yes --> C{Ready to publish\nor archive?}
    C -- Yes --> D{Discipline-specific\nrepository exists?}
    D -- Yes --> E[📦 Discipline repo\ne.g. GEO, ENA, Zenodo]
    D -- No --> F[📦 UCL Research\nData Repository - RDR]

    C -- No --> G{Sensitive?\ne.g. patient data}
    G -- Yes --> H[🔒 Data Safe Haven\nor TRE]
    G -- No --> I[🗄️ RDSS]

    B -- No --> J{Personal or\nsmall group?}
    J -- Yes --> K{Large files?\ne.g. PPTs, big exports}
    K -- Yes --> L[💾 S Drive]
    K -- No --> M[☁️ OneDrive]
    J -- No --> N[🏢 SharePoint]

    style H fill:#fee2e2
    style E fill:#dcfce7
    style F fill:#dcfce7
    style I fill:#dbeafe
```

> ⚠️ **HPC scratch (Myriad `/scratch`, `/tmpdir`)** is not storage — always move outputs to RDSS or your local machine promptly. See the HPC guide for details.

---

## Storage options at a glance

| Service | For | Size | Cost | Backed up | External sharing |
|---|---|---|---|---|---|
| **RDSS** | Unpublished research data | 1TB free, expandable | free at point of use, ~£50/TB/yr should be charged to grants where possible | Yes | Yes (recently added) |
| **RDR** | Published / archived datasets | 50GB/person (increasable) | Free | Yes (long-term) | Public (DOI issued) |
| **DSH / TRE** | Sensitive/identifiable data | Varies | Contact ISD | Yes | Restricted |
| **S Drive** | Non-research data | 200GB+ | Free up to limit; £0.15/GB/3yr beyond | Yes (hourly) | UCL only |
| **OneDrive** | Light personal/collaborative docs | 100GB | Free (via UCL subscription) | Yes | Yes |
| **SharePoint** | Departmental/team/wider UCL content | Varies | Free | Yes | Yes |

---

## Service details

### RDSS — Research Data Storage Service
**Use for:** any and all research data

**Key facts:**
- UCL research data policy states research data should be stored on the RDSS
- Projects are created by the **PI** at [storageadmin.rd.ucl.ac.uk](https://storageadmin.rd.ucl.ac.uk/projects/new) (UCL network required); generally processed within a few days
- Staff and students can be admins/members — good for large collaborative projects
- 1TB free; request more through the same portal (cost to grant where possible)
- **File limit:** initial limit of 200,000 files per project. Large projects can request a higher limit through MyServices.
- **Project duration:** initially 5 years; extensions can be requested through the RDSS admin portal.
- Storage usage visible at [storageadmin.rd.ucl.ac.uk](https://storageadmin.rd.ucl.ac.uk) — updated overnight, not live. `du -sh` from an rdss project directory will show _double_ the actual size due to the mirrored storage system. Expected behaviour - good to be aware of.
- External collaborators can now be granted direct access
- **Roll accounts** - **Nick** to add something here. ********************************
- **Nick** to add point about projects with large files
 
**Gotchas:**
- You must be on the UCL network (or VPN) to create, manage or access a project

**Tips:**
- Structure your project directory from day one — it's painful to reorganise later when the project has 10 members
- Set up a `scratch/` or `tmp/` subdirectory for intermediate files so the important stuff is easy to find
- PhD students: make sure your PI has set up the RDSS project before you start generating data

**Project Setup/Structure**
- *Nick* to add something here.

---

### RDR — UCL Research Data Repository
**Use when:** a project is ending or a paper is being submitted and there is no domain-specific repository available.

**Key facts:**
- Data is **publicly accessible** and assigned a DOI — treat it as permanent publication
- 50GB per-person upload limit by default; contact [researchdata-support@ucl.ac.uk](mailto:researchdata-support@ucl.ac.uk) to increase
- Discipline-specific repositories (GEO, ENA, ArrayExpress, Zenodo, etc.) should be considered first where they exist — they're more discoverable by your community

**Gotchas:**
- Once data is deposited and public, you cannot easily unpublish it — make sure you have consent/ethics approval to share before uploading
- The 50GB default limit is low for some projects; request an increase early, not the day before submission

**Tips:**
- Check your funder's preferred repository before depositing (UKRI often accepts Zenodo; Wellcome prefers specific repos for certain data types)
- Deposit raw data, not just processed outputs — reviewers and future researchers will thank you
- Identify the appropriate metadata and submit as much as possible

---

### TRE / DSH —  Trusted Research Environment and Data Safe Haven
**Use when:** data contains sensitive or identifiable information, e.g. NHS patient records, linked administrative data, or anything requiring ethical controls on access.

**Key facts:**
- ARC has a new TRE with more compute flexibility; DSH is also still available
- Access and egress are controlled and audited
- Contact ARC to discuss your project before starting — setup takes time

**Gotchas:**
- Do not store sensitive data on RDSS, OneDrive, or S Drive, even temporarily
- Getting a project approved can take weeks — factor this into project timelines

---

### S Drive
**Use when:** a team needs a shared working space for non-research files (admin, presentations, meeting notes, etc.).

- 200GB+ for staff; additional space purchasable at £0.15/GB for 3 years
- Hourly backups
- Not designed for large research data volumes — use RDSS for that

---

### OneDrive
**Use when:** you need to sync and share lightweight documents across devices, or collaborate on Office files with internal or external colleagues.

- 100GB per user via UCL's Microsoft 365 subscription
- Easy external sharing, works across devices
- Not appropriate for primary research data storage — think of it as a working/collaboration layer

---

### SharePoint
**Use when:** you're managing content for a wider team, department, or project that needs structured document management and broader access.

- Good for lab wikis, shared protocols, department resources
- Not appropriate for large or sensitive research datasets
- Ongoing project to move SharePoint projects to data hubs - more info on its way

---

## A note on funder requirements

Most major funders now require a **Data Management Plan (DMP)** at application stage and open data deposition on publication. Key points:

- **UKRI** (BBSRC, MRC, NERC, etc.): requires a DMP; data should be made available with minimal restrictions, usually within 12 months of publication. Zenodo and discipline-specific repos are acceptable.
- **Wellcome**: requires open access data deposition; has specific guidance for genomics, imaging, and clinical data types.
- **Horizon Europe**: open data by default; DMPs required.

UCL's [Research Data Management Team](https://library-guides.ucl.ac.uk/research-data-management/writing) can advise on DMPs and help identify the right repository. The [DMP Online tool](https://dmponline.dcc.ac.uk/) has funder-specific templates.

---

## Further help

| Need | Contact |
|---|---|
| RDSS project setup, storage limits, file count issues | [researchdata-support@ucl.ac.uk](mailto:researchdata-support@ucl.ac.uk) |
| DSH / TRE access | ARC |
| DMP advice, RDR deposits | [researchdata-support@ucl.ac.uk](mailto:researchdata-support@ucl.ac.uk) |
| HPC storage (Myriad scratch, Lustre) | See [HPC guide](https://github.com/UCL-Biosciences/Biosciences-Comp-Support/blob/main/UCL_comp_guides/high_performance_compute_at_UCL.md) |
