DOCUMENT OF UNDERSTANDING
SAP SD • CUSTOMER EDI • KNOWLEDGE TRANSFER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Focus: SAP SD order-to-cash, automotive EDI, IDoc processing and production support


1. Executive Summary
This Document of Understanding presents understanding of customer-facing EDI business processes in SAP ERP. The document consolidates the KT topics into a structured view of process ownership, message flows, IDoc architecture, monitoring, and support responsibilities.


Key capability statement
Translate customer EDI requirements and implementation guidelines into SAP SD process and mapping requirements.
Understand inbound and outbound IDoc lifecycles, including control, data and status records.
Support EDI-driven customer processes across order management, scheduling agreements, consignment, ASN and invoicing.
Investigate failures through SAP monitoring, status analysis, application logs and functional coordination.
Work effectively across functional EDI, SCM, logistics and FI teams while respecting regional ownership and ticket-routing models.
Evidence base
Prepared from the supplied “KT-session TCS – EDI supported business processes” presentation and its associated knowledge-transfer transcript. The source material describes the Schaeffler pre-merger SAP EP1 landscape and related EDI operations; system names, custom objects and team assignments should therefore be validated against the current production organization before formal use.
2. Consultant Profile & Scope of Understanding

Scope boundaries
This DOU describes understanding of the processes presented in the KT session; it does not claim ownership of every custom development, interface or regional support queue.
Customer-specific EDI guidelines remain the controlling source for segment usage, qualifiers, field positions and partner-specific deviations.
Current organizational assignments, system landscape and ticket groups should be reconfirmed before operational execution.
3. EDI & Message Standards Understanding
Electronic Data Interchange (EDI) is the structured exchange of routine business documents between computer systems using agreed message standards. In the KT context, EDI reduces manual entry, accelerates transmission and supports accurate, repeatable business processing between customers, suppliers, carriers, warehouses and ERP systems.
Standards and formats covered

Implementation principle: the customer’s implementation guideline is authoritative, including partner-specific conventions for articles, material numbers, purchase-order references and qualifiers.
Practical message-reading approach
Start with the message envelope and identify the sender, receiver, message type and interchange reference.
Read segment identifiers and qualifiers before interpreting the values.
Locate partner, material, purchase-order, schedule and quantity/date information at the correct hierarchy level.
Validate interpretation against the customer’s implementation guideline before designing or troubleshooting SAP mapping.
4. SAP SD / Customer EDI Process Coverage
The following matrix consolidates the customer-EDI process coverage described in the KT material.



5. Integration Architecture & IDoc Lifecycle
The KT material describes SAP EP1 as the ERP platform connected to an EDI subsystem using IBIS / Axway TradeSync Integration Manager. External EDI formats are transformed into SAP IDocs for inbound processing, and SAP IDocs are transformed into partner-specific formats for outbound delivery.
Conceptual flow

IDoc structure

Inbound DELINS / scheduling-agreement release
IDoc arrives in status 64 and waits for background processing.
Processing code from WE20 invokes the configured inbound flow, including pre-checks and standard function-module processing.
Customer-specific extensions, field adjustments, BAdIs and user exits may be applied; errors are routed to the relevant monitor/error-handling process.
On success, the scheduling-agreement release is updated and processing information/flags are written for monitoring and follow-up.
Outbound ASN / SHPMNT
Shipment loading reaches the relevant completion status and triggers the outbound message flow.
Pre-checks validate shipment information before SHPMNT IDoc creation.
BAdIs/user exits and post-processing adjust standard fields and extensions as required.
The SHPMNT05 IDoc is transformed by the EDI subsystem into the customer’s agreed external format.
6. Direct Shipment, Consignment & Billing Understanding
The session explained a direct-shipment scenario in which customer messages enter the EDI subsystem, create or update sales-order activity in SAP EP1, and result in outbound order responses, shipping notifications and invoices. A cross-company relationship may exist between the production company/plant and the sales-order company/sales organization.
Key functional points
Forecast releases support planning and longer-term demand; shipping schedules communicate direct, date-specific requirements.
Sales-order confirmations may split quantities across multiple dates when the requested quantity cannot be confirmed on one date.
Shipping advice informs the customer when goods are expected to arrive at its plant.
Consignment terminology must be distinguished from transport/loading concepts; the KT specifically differentiates shipment/consignment handling from multi-stop truck-load transport.
Billing and self-billing messages complete the customer-facing order-to-cash exchange.


7. Operating Model, Ownership & Collaboration
The KT material presents a regional and functional support model. Assignment groups and ownership may evolve with organizational changes, so the model below should be treated as the session baseline and verified before use.

Support approach
Classify the issue by process, message type, direction, customer/region and SAP document impact.
Confirm whether the issue is data, configuration, mapping, middleware, SAP processing or master-data related.
Coordinate with the correct regional/functionally accountable team rather than routing solely by symptom.
Document the root cause, correction, reprocessing result and any preventive action.
8. Monitoring, Error Handling & Resolution Method
The KT references SAP monitors for arriving forecasts/JIT releases, incoming orders, self-billing procedures and EDI messages. These monitors support operational visibility into light status, IDoc number, sender, creation date, message type and processing status.
Recommended triage sequence
Identify the business process and direction (inbound/outbound).
Capture the IDoc number, message type, sender/receiver, creation time and related SAP document.
Review control, data and status records; determine the last successful status and the failure point.
Validate master data and customer-specific rules, including material/customer-material mapping, partner profile, schedule agreement and required dates/quantities.
Check whether the issue is in EDI transformation, SAP pre-check, standard function module, BAdI/user exit, application document creation or post-processing.
Correct the root cause through the approved process, then reprocess and verify the resulting SAP document and outbound acknowledgement/message.
Record the resolution and communicate impact, workaround and prevention to stakeholders.


9. Formal Understanding & Acknowledgement
By signing below, the undersigned acknowledge that this DOU accurately summarizes the scope of knowledge transfer reviewed and the professional understanding. The DOU is a capability and alignment record; it does not replace project-specific design documents, customer implementation guides, security procedures or formal approval workflows.
Appendix A — Reference Terms

Prepared from supplied KT materials • Professional summary • Validate against current project documentation before operational use
