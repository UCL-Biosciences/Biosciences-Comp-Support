---
layout: default
title: Data Sharing & Transfer Guide
nav_order: 3
has_children: false
---

# Data Sharing & Transfer Guide — UCL Biosciences

**Note:** This is a work-in-progress — some details may need updating/amending.

> **Who is this for?** PIs, postdocs, PhD students, and professional services staff who need to share research data with collaborators, transfer large files, or make data publicly available.
> 
> A separate guide covers [storage options](/Biosciences-Comp-Support/guides/storage/) (RDSS, RDR, OneDrive, etc.) and [HPC-specific storage](/Biosciences-Comp-Support/guides/hpc/).

---

## Before you share: two questions

### 1. Live or one-off?

| You want to… | Approach |
|---|---|
| Give a collaborator ongoing access to a folder that stays in sync | Share access to RDSS, SharePoint, S Drive or OneDrive directly — they always see current files |
| Send a snapshot of files as they are now | Export/download and share a static file or archive (zip/tar) |
| Make data permanently citable and public | Deposit to RDR or a domain repository — files are frozen at deposit |

### 2. How sensitive is the data?

If data contains anything identifiable — patient records, linked administrative data, personal information — **stop and contact ISD or ARC before doing anything else**. The DSH/TRE is the only appropriate system for this data.

For all other data, continue below.

---

## Quick decision guide

```mermaid
flowchart TD
    A([Start]) --> B{Sensitive /<br/>identifiable?}
    B -- Yes --> C["🔒 DSH / TRE only<br/>Contact ISD first"]
    B -- No --> D{Ready to publish<br/>or archive?}
    D -- Yes --> E["📦 Domain repository or RDR<br/>GEO, ENA, Zenodo, RDR…"]
    D -- No --> F{File size?}
    F -- "<20 MB" --> G["Email attachment<br/>snapshot only"]
    F -- "<100 MB" --> H["Teams attachment<br/>up to 100MB"]
    F -- ">10 GB" --> I["☁️ OneDrive or SharePoint link<br/>good for live links"]
    F -- ">10 GB" --> J["📡Globus (resumable, overnight-safe)<br/>or RDSS for sharing large files"]

    style C fill:#fee2e2
    style E fill:#dcfce7
    style G fill:#dbeafe
    style H fill:#dbeafe
    style I fill:#dbeafe
    style J fill:#dbeafe
```

{: .danger }
> **Never use personal email, WeTransfer, or USB drives for research data.** These bypass UCL data governance and may breach funder or ethics requirements.

---

## Sharing options at a glance

All options below share **live files** — recipients always see the current state, not a snapshot — except RDR and domain repositories, where deposits are **frozen at upload** and cannot be updated.

| Method | Best for | Practical size limit | External | VPN required | Live files |
|---|---|---|---|---|---|
| **RDSS — direct access** | Ongoing collaboration | TB scale | Yes (PI grants) | To manage via storageadmin; not for recipient | Yes |
| **RDSS — shared link** | One-off access to specific files | TB scale | Yes | No | Yes |
| **OneDrive link** | Small files, Office docs, quick shares | MBs up to few GB | Yes | No | Yes |
| **SharePoint** | Team/departmental documents | Varies | Yes | No | Yes |
| **Globus** | Large/bulk transfers, HPC-to-HPC | Effectively unlimited | Yes | No | Yes |
| **RDR** | Published / archived datasets | 50 GB default | Public (DOI) | No | **No — frozen at deposit** |
| **Domain repository** | Published data in your field | Varies | Public | No | **No — frozen at deposit** |
| **DSH / TRE** | Sensitive / identifiable data | Varies | Controlled | Inside TRE only | Yes |

---

## Permissions

### Who can do what

| Action | Who |
|---|---|
| Add/remove members, set folder permissions | PI or designated project admin |
| Grant external collaborator access to RDSS | PI or admin, via [storageadmin.rd.ucl.ac.uk](https://storageadmin.rd.ucl.ac.uk) (UCL network or VPN required) |
| Share an OneDrive or SharePoint link | Any UCL user |
| Set link expiry or restrict to view-only | Any UCL user (in the share dialog) |
| Request a Globus endpoint | Any UCL user via [rc-support@ucl.ac.uk](mailto:rc-support@ucl.ac.uk) |
| Deposit to RDR | Any UCL researcher |

### RDSS folder permissions

Permissions can be scoped per folder: read, read/write, or read/write/execute. Use this to give collaborators access only to what they need — for example, a `data/shared/` subdirectory rather than the entire project.

### Link permissions (OneDrive / SharePoint / RDSS)

When sharing via link, always consider:

- **View-only vs edit** — use view-only unless the recipient needs to add or change files
- **Expiry date** — set one for any external share; there is no automatic expiry
- **Password protection** — available for OneDrive links; useful for anything going outside UCL
- **Specific people vs anyone with the link** — prefer specific people where possible

### Guest / external account setup

External collaborators need either a UCL guest account or an institutional account UCL's systems recognise. For RDSS access:

- [Current process](https://www.ucl.ac.uk/advanced-research-computing/how-access-rdss-external-collaborator) says you need a UCL Visitor account and a "UCL RDSS project" email with project detail
- Plan ahead: don't leave this until a collaborator is already waiting for data
- For Globus, external collaborators use their own institutional credentials — no UCL account needed *(this needs verifying)*

---

## Practical transfer considerations

### File size

File size affects which method is practical rather than which is permitted. For small files, email attachments or OneDrive links are fine. As files get larger — multi-GB datasets, image stacks, sequencing libraries — you need a more robust method.

### Upload speed and reliability

Network connection makes a large difference for anything over a few GB:

- **Wired ethernet on campus** — fastest and most reliable; use this for large transfers where possible
- **Eduroam (campus Wi-Fi)** — adequate for moderate transfers but shared bandwidth; avoid peak hours (10am–3pm) for anything substantial
- **Home broadband** — upload speeds are typically 10–50 Mbps; a 100 GB transfer can take several hours. Use Globus rather than browser-based tools — it handles dropped connections and resumes
- **Off-peak scheduling** — Globus transfers can be left to run overnight without supervision; prefer this for anything over ~50 GB
- As a rough guide: 100 GB at 50 Mbps upload takes around 4–5 hours; on a 1 Gbps campus connection, around 15 minutes

### VPN

UCL's GlobalProtect VPN is required to access some systems from off-campus:

- **Required:** storageadmin portal (to manage RDSS projects and permissions), S Drive, some legacy UCL services
- **Not required:** OneDrive, SharePoint, RDR, Globus transfers, RDSS shared links

If you are managing a project or setting up external access remotely, connect to VPN first. VPN setup instructions: [ucl.ac.uk/isd/services/get-connected/ucl-virtual-private-network-vpn](https://www.ucl.ac.uk/isd/services/get-connected/ucl-virtual-private-network-vpn)

### Transferring from HPC (Myriad)

Myriad scratch is not backed up and is subject to purge — do not leave data there waiting to be transferred. When a job completes:

1. Move outputs to **RDSS** promptly via `rsync` or the file manager
2. For large datasets going to an external collaborator, stage on RDSS then use **Globus** to transfer
3. Do not treat scratch as a staging area for more than a day or two

See the [HPC guide](/Biosciences-Comp-Support/guides/hpc/) for Myriad scratch policies and mounting RDSS on the cluster.

### Format considerations

- **Many small files** (Nanopore fast5/pod5, image stacks) transfer slowly and hit the RDSS file count limit (200,000 files/TB) faster than the storage limit — consider archiving to `tar` first or using HDF5/Zarr
- **Checksums** — verify integrity for large transfers with `md5sum` or `sha256sum` at both ends; Globus does this automatically, manual transfers do not
- **Compression** — often not worthwhile for already-compressed formats (FASTQ.gz, CRAM, PNG)

---

## Further help

| Need | Contact |
|---|---|
| RDSS external access, guest accounts, project setup | [researchdata-support@ucl.ac.uk](mailto:researchdata-support@ucl.ac.uk) |
| Globus endpoint setup, HPC transfers | [researchdata-support@ucl.ac.uk](mailto:researchdata-support@ucl.ac.uk) |
| DSH / TRE access | ISD / ARC |
| VPN setup | [ISD VPN guidance](https://www.ucl.ac.uk/isd/services/get-connected/ucl-virtual-private-network-vpn) |
| HPC storage and scratch policies | See [HPC guide](/Biosciences-Comp-Support/guides/hpc/) |
