---
name: professional-doc
description: Generate professional business documents (Invoices, Work Orders, Quotes, Contracts) with JW Ventures branding. Use keywords: invoice, work order, quote, contract, estimate, billing, proforma.
argument-hint: [type] [client] [amount] [service]
user-invocable: true
---

# Professional Document Generator

**Purpose:** Generate properly formatted business documents with JW Ventures branding for UniPlay platform clients.

**Supported Document Types:**
- Invoice
- Work Order
- Quote / Estimate
- Proforma Invoice
- Service Agreement

---

## JW Ventures Company Info (Default)

```
Company: JW Ventures Brunei
Registration: P30000657
Address: Bandar Seri Begawan, Brunei Darussalam
Email: info@jwventure.workers.dev
Bank: Baiduri Bank
```

---

## Document Templates

### 1. INVOICE

**Use when:** Billing for completed services or requesting payment.

**Required Fields:**
- Invoice Number (format: INV-YYYY-### or client-specific)
- Invoice Date
- Due Date
- Client Name & Company
- Line Items (Description, Qty, Unit Price, Amount)
- Total Amount
- Payment Reference

**Template Structure:**
```
JW Ventures Brunei header
Company details
Bill To section
Invoice details (number, date, due)
Items table
Subtotal / Tax / Total
Payment details
Footer: JW Ventures | P30000657 | Bandar Seri Begawan | info@jwventure.workers.dev
```

**Signature:** Only JW Ventures signs (service provider)

---

### 2. WORK ORDER

**Use when:** Getting client approval before starting work.

**Required Fields:**
- Work Order Number
- Date
- Client Name
- Services/Items to be delivered
- Total Cost
- Both signatures required

**Template Structure:**
```
Title: WORK ORDER: [Service Name]
Client info
Overview/Scope section
Services table (Service, Description, Fee)
Benefits/What You Get section
Acceptance section
SIGNATURES (Side-by-side table):
  - LEFT: JW Ventures (Jabbar, Managing Director)
  - RIGHT: Client (Name, Title)
Payment Details
Footer
```

**Signature:** BOTH parties sign (JW Ventures + Client)

---

### 3. QUOTE / ESTIMATE

**Use when:** Providing pricing for potential work (not yet approved).

**Required Fields:**
- Quote Number
- Valid Until Date
- Client Name
- Line Items with pricing
- Total
- Notes about validity

**Template Structure:** Similar to Invoice, but with "Valid Until" instead of "Due Date"

**Signature:** Only JW Ventures signs

---

### 4. SERVICE AGREEMENT / CONTRACT

**Use when:** Formal contract for ongoing services or major milestones.

**Required Fields:**
- Contract Number
- Effective Date
- Both parties
- Scope of Work
- Payment Terms
- Duration
- Signatures

**Signature:** BOTH parties sign

---

## Execution Instructions

### Step 1: Extract Parameters
Identify from user request:
- **Document type:** invoice, work order, quote, contract
- **Client name:** e.g., PickleballBN, Racquet & Co
- **Amount:** total value
- **Service:** brief description
- **Items:** (optional) detailed line items

### Step 2: Generate Document
Use Python `python-docx` to create the document with:
- Proper headers
- Company branding
- Correct template for document type
- Appropriate signature sections

### Step 3: Output Format
Always create both:
1. Markdown source (.md) - for reference/version control
2. DOCX file (.docx) - for client delivery

### Step 4: Naming Convention
```
[DOCTYPE]_[Client]_[Service]-FINAL.docx
Example: INVOICE_PickleballBN_Domain_Migration-FINAL.docx
```

---

## File Location for Output

Always save to:
```
C:\uniplay-development\docs\client\pickleballbn\[FOLDER]\
```

Or if specified by user:
```
C:\uniplay-development\docs\client\[CLIENT_NAME]\
```

---

## Numbering System

| Prefix | Use | Example |
|--------|-----|---------|
| INV- | Standard Invoice | INV-2026-001 |
| DM- | Domain Migration | DM-2026-001 |
| M#- | Milestone | M2-2026-001 |
| WO- | Work Order | WO-2026-001 |
| QT- | Quote | QT-2026-001 |

---

## Common Line Items (Domain Services)

| Item | Typical Price |
|------|---------------|
| Domain Transfer Coordination | BND 100 |
| DNS Configuration | BND 50 |
| SSL Certificate Setup | BND 50 |
| Domain Registration (.com) | BND 15-20/year |
| Domain Registration (.com.bn) | BND 150/year |
| Email Setup | BND 30-50 |
| Hosting Setup | BND 50-100 |

---

## Common Line Items (Development Services)

| Item | Typical Price |
|------|---------------|
| Initial Consultation | BND 100-200 |
| Requirement Analysis | BND 300-500 |
| UI/UX Design | BND 500-1500 |
| Frontend Development | BND 50-100/hour |
| Backend Development | BND 50-100/hour |
| Integration | BND 200-500 |
| Testing & QA | BND 200-400 |
| Deployment | BND 150-300 |

---

## Footer (All Documents)

```
JW Ventures Brunei | P30000657 | Bandar Seri Begawan | info@jwventure.workers.dev
```

- Center aligned
- Font size: 9pt
- Appears on every page

---

## Signature Rules Summary

| Document Type | JW Ventures Signs | Client Signs |
|---------------|-------------------|--------------|
| Invoice | Yes (optional) | No |
| Work Order | Yes | Yes |
| Quote | Yes | No |
| Contract | Yes | Yes |
| Proforma | Yes | No |
| Receipt | Yes | No |

---

## Examples

### User Request:
```
Create invoice for PickleballBN, domain migration service, BND 215
```

### My Response:
1. Create `INVOICE_PickleballBN_Domain_Migration-FINAL.docx`
2. Include line items: Domain Transfer (100), DNS (50), Registration (15)
3. Add payment details and footer
4. Output file path confirmation

---

### User Request:
```
Create work order for Chia, premium domain setup, BND 300
```

### My Response:
1. Create `WORK_ORDER_Premium_Domain-FINAL.docx`
2. Side-by-side signature table
3. Both Jabbar and Chia signature sections
4. Payment details
5. Footer

---

## Notes

- Always use BND currency for Brunei clients
- Tax is typically 0% (Brunei no GST)
- Always include "Separate from M2/Milestone deliveries" note when applicable
- For UniPlay clients, emphasize SaaS model (UniPlay owns infrastructure)
